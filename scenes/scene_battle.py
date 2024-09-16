from enum import Enum
from typing import List, Optional

import pygame
from select import select

from managers.Entities import Monster, Entity, Player
from managers.EntityManager import MonsterManager
from managers.MapManager import MapManager
from util.FightData import FightData
from util.PlayerData import PlayerData
from util.Skill import Skill, Need
from util.Util import Image

"""
Example Scene
"""

# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager):
    global manager
    global fight_background
    global enemy_arr
    global ally_arr
    global fight_data
    global selected_unit
    global my_turn
    global ally_button_arr
    global enemy_button_arr
    global state
    global unit_select
    global skill_card
    global needed_data
    global black_background
    global mouse_pos
    global unit_select_red
    global next_turn_button
    global log
    global game_font

    mouse_pos = (0, 0)
    selected_unit = None
    ally_button_arr = []
    enemy_button_arr = []
    state = State.NoPlayer
    needed_data = []
    log = "전투 시작!"

    manager = scene_manager
    fight_background = Image("assets/fight/fight_bg.jpg").scale(1920, 1080)
    unit_select = Image("assets/UI/unit_select.png").scale(128, 128)
    unit_select_red = Image("assets/UI/unit_select_red.png").scale(128, 128)
    skill_card = Image("assets/UI/empty_card.png").scale(256, 256)
    next_turn_button = Image("assets/UI/next.png").scale(256, 256).button(1800, 800, lambda: next_turn(), is_center=True)
    black_background = Image("assets/UI/black.png").scale(1920, 1080)
    black_background.image = black_background.image.convert_alpha()
    black_background.image.set_alpha(200)
    game_font = pygame.font.Font(r"assets\font\neodgm_code\neodgm_code.ttf", 30)


    json_data = MapManager.map_data
    map_data = json_data['stage'][MapManager.cur]

    enemies: List[Optional[Monster]] = [MonsterManager.get(i['id'], i['lvl']) for i in map_data['enemies'] if i]
    for i in range(4-len(enemies)):
        enemies.append(None)

    fight_data = FightData(PlayerData.party, enemies)
    for i in range(len(fight_data.ally)):
        if fight_data.ally[i] is not None:
            ally_i__image = fight_data.ally[i].image
            ally_i__image.image = ally_i__image.image.convert_alpha()
            ally_button_var = ally_i__image.scale(128, 128).button(i * 150 + 200, 540, is_center=True,
                                                                   on_click=lambda j=i: click_obj(
                                                                                fight_data.ally[j]))
            ally_button_arr.append(ally_button_var)
            for j in range(len(fight_data.ally[i].skills)):
                skills_j_ = fight_data.ally[i].skills[j]
                skills_j_.button = skill_card.button(get_x(j, fight_data.ally[i].skills), 952, is_center=True,
                                              on_click=lambda k=j: click_sk(k))
                skills_j_.image = skills_j_.image.scale(68 * (256 / 96), 68 * (256 / 96))
            ally_button_arr[-1].loc = fight_data.ally[i]
            fight_data.ally[i].used = False
        else:
            ally_button_arr.append(None)

    for i in range(len(fight_data.enemy)):
        if fight_data.enemy[i] is not None:
            i__image = fight_data.enemy[i].image
            i__image.image = i__image.image.convert_alpha()
            enemy_button_var = i__image.scale(128, 128).flip(True, False).button(i * 150 + 1270, 540,
                                                                              is_center=True,
                                                                              on_click=lambda
                                                                                                   j=i: click_obj(
                                                                                                   fight_data.enemy[j]))
            enemy_button_arr.append(enemy_button_var)
        else:
            enemy_button_arr.append(None)

def next_turn():
    global state
    add_log("아군 턴 종료!")
    cancel()
    state = State.EnemyTurn
    for i in fight_data.ally:
        if i is not None:
            i.used = False

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    global state, selected_unit, target, mouse_pos
    if event.type == pygame.MOUSEMOTION:
        mouse_pos = event.pos
    if event.type == pygame.MOUSEBUTTONDOWN:
        clicked = False
        clicked = check_click_obj_iter(clicked, event)
        if (state is State.PlayerSelected or state is State.SkillSelected) and isinstance(selected_unit, Player):
            for i in selected_unit.skills:
                ret = i.button.check_click(event.pos)
                if ret:
                    clicked = True
        if state is State.NoPlayer or state is State.PlayerSelected:
            ret = next_turn_button.check_click(mouse_pos)
            if ret:
                clicked = True
        if not clicked:
            click_obj(None)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_c:
            #cancel
            cancel()
    pass


def cancel():
    global state, selected_unit, target
    state = State.NoPlayer
    selected_unit = None
    target = None


def check_click_obj_iter(clicked, event):
    for e in ally_button_arr:
        if e is None:
            continue
        ret = e.check_click(event.pos)
        if ret:
            clicked = True
    for e in enemy_button_arr:
        if e is None:
            continue
        ret = e.check_click(event.pos)
        if ret:
            clicked = True
    return clicked


def click_obj(i: Optional[Entity]):
    global selected_unit, state
    if (state is State.NoPlayer or state is State.PlayerSelected):
        if i is None:
            state = State.NoPlayer
        elif isinstance(i, Player):
            if i.used is False:
                selected_unit = i
        else:
            selected_unit = i
    if selected_unit is not None and state is State.NoPlayer:
        state = State.PlayerSelected
    if state is State.SkillSelected and i is not None:
        global target
        selected_unit.used = True
        if (target.need_data is Need.Any) or (target.need_data is Need.Self and i is selected_unit) or (target.need_data is Need.Ally and isinstance(i, Player)) or (target.need_data is Need.Enemy and isinstance(i, Monster)):
            result = target.activate(selected_unit, fight_data, i)
            add_log(result)
            cancel()
        else:
            selected_unit.used = False


    pass


def add_log(result):
    global log
    if log is None:
        log = ""
    log += "\n" + result


def click_sk(i: int):
    global state, target
    target = selected_unit.skills[i]
    if state is State.PlayerSelected:
        state = State.SkillSelected
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    global mouse_pos, state, log_output
    for i in range(len(fight_data.enemy)):
        if fight_data.enemy[i] is None:
            continue
        if fight_data.enemy[i].hp_c <= 0:
            add_log(fight_data.enemy[i].name + "이(가) 사망했다!")
            fight_data.enemy[i] = None
    if all(item is None for item in fight_data.enemy):
        if state is not State.Fin:
            add_log("승리했다!")
            state = State.Fin
    for i in range(len(fight_data.ally)):
        if fight_data.ally[i] is None:
            continue
        if fight_data.ally[i].hp_c <= 0:
            add_log(fight_data.ally[i].name + "이(가) 사망했다!")
            fight_data.ally[i] = None

    if state is State.EnemyTurn:
        for i in range(len(fight_data.enemy)):
            if fight_data.enemy[i] is None:
                continue
            result = fight_data.enemy[i].action(fight_data)
            add_log(result)
        add_log("적군 턴 종료!")
        state = State.NoPlayer
    pass

    log_output = [game_font.render(i, True, (0, 0, 0)) for i in log.splitlines()[-5:]]


# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):

    fight_background.draw(screen, 0, 0)
    for i in range(len(log_output)):
        screen.blit(log_output[i], (0, i*30))
    if not (state is State.NoPlayer or state is State.EnemyTurn) and isinstance(selected_unit, Player):
        skills_num = selected_unit.skills
        for j in range(len(skills_num)):
            skills_num[j].button.draw(screen)
            skills_num[j].image.draw(screen, get_x(j, skills_num), 1080-256+35*(256/96), is_center=True)

    if selected_unit:
        if isinstance(selected_unit, Player):
            x = fight_data.ally.index(selected_unit)*150+200
        else:
            x = fight_data.enemy.index(selected_unit)*150+1270
        unit_select.draw(screen, x, 600, is_center=True)
    for i in range(len(ally_button_arr)):
        if fight_data.ally[i] is not None:
            if ally_button_arr[i].loc.used:
                ally_button_arr[i].image.set_alpha(200)
            else:
                ally_button_arr[i].image.set_alpha(255)
            ally_button_arr[i].draw(screen)

    for i in range(len(enemy_button_arr)):
        if fight_data.enemy[i] is not None:
            enemy_button_arr[i].draw(screen)

    next_turn_button.draw(screen)
    if state is State.SkillSelected:
        black_background.draw(screen, 0, 0)
        skills_num = selected_unit.skills
        for j in range(len(skills_num)):
            if skills_num[j] is target:
                skills_num[j].button.draw(screen)
                skills_num[j].image.draw(screen, get_x(j, skills_num), 1080-256+35*(256/96), is_center=True)
        for i in range(len(ally_button_arr)):
            if fight_data.ally[i] is not None:
                if (target.need_data is Need.Ally or target.need_data is Need.Any):
                    if ally_button_arr[i].check_click(mouse_pos):
                        unit_select_red.draw(screen, ally_button_arr[i].rect.centerx, 600, is_center=True)
                    ally_button_arr[i].draw(screen)

                if  (target.need_data is Need.Self and ally_button_arr[i].loc is selected_unit):
                    unit_select.draw(screen, ally_button_arr[i].rect.centerx, 600, is_center=True)
                    if ally_button_arr[i].rect.collidepoint(mouse_pos):
                        unit_select_red.draw(screen, ally_button_arr[i].rect.centerx, 600, is_center=True)
                    ally_button_arr[i].draw(screen)

        for i in range(len(enemy_button_arr)):
            if fight_data.enemy[i] is not None:
                if target.need_data is Need.Enemy or target.need_data is Need.Any:
                    if enemy_button_arr[i].rect.collidepoint(mouse_pos):
                        unit_select_red.draw(screen, enemy_button_arr[i].rect.centerx, 600, is_center=True)
                    enemy_button_arr[i].draw(screen)







def get_x(j, skills_num):
    gap = (96-26)*(256/96)
    j_ = 960 + (-gap / 2 * (len(skills_num) - 1) + gap * j)
    return j_


# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass

class State(Enum):
    NoPlayer = 0
    PlayerSelected = 1
    SkillSelected = 2
    Target1Selected = 3
    Target2Selected = 4
    EnemyTurn = 5
    Fin = 6