from enum import Enum
from typing import List, Optional

import pygame
from select import select

from managers.Entities import Monster, Entity, Player
from managers.EntityManager import MonsterManager
from managers.MapManager import MapManager
from util.FightData import FightData
from util.PlayerData import PlayerData
from util.Skill import Skill
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
    global ally_button
    global enemy_button
    global state
    global unit_select
    global skill_card

    selected_unit = None
    ally_button = []
    enemy_button = []
    state = State.NoPlayer

    manager = scene_manager
    fight_background = Image("assets/fight/fight_bg.jpg").scale(1920, 1080)
    unit_select = Image("assets/UI/unit_select.png").scale(128, 128)
    skill_card = Image("assets/UI/empty_card.png").scale(256, 256)

    json_data = MapManager.map_data
    map_data = json_data['stage'][MapManager.cur]


    enemies: List[Optional[Monster]] = [MonsterManager.get(i['id'], i['lvl']) for i in map_data['enemies'] if i]
    for i in range(4-len(enemies)):
        enemies.append(None)

    fight_data = FightData(PlayerData.party, enemies)

    for i in range(len(fight_data.ally)):
        if fight_data.ally[i] is not None:
            ally_button.append(fight_data.ally[i].image.scale(128, 128).button(i * 150 + 200, 540, is_center=True, on_click=lambda j=i: click_obj(fight_data.ally[j])))
        else:
            ally_button.append(None)

    for i in range(len(fight_data.enemy)):
        if fight_data.enemy[i] is not None:
            enemy_button.append(fight_data.enemy[i].image.scale(128, 128).flip(True, False).button(i * 150 + 1270, 540, is_center=True, on_click=lambda j=i:click_obj(fight_data.enemy[j])))
        else:
            enemy_button.append(None)

    for i in fight_data.ally:
        for j in range(len(i.skills)):
            i.skills[j].button = skill_card.button(get_x(j, i.skills), 952, is_center=True, on_click=lambda k=j: click_sk(k))
            i.skills[j].image = i.skills[j].image.scale(68*(256/96), 68*(256/96))

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        clicked = False
        for e in ally_button:
            ret = e.check_click(event.pos)
            if ret:
                clicked = True
        for e in enemy_button:
            ret = e.check_click(event.pos)
            if ret:
                clicked = True
        if state is State.PlayerSelected and isinstance(selected_unit, Player):
            for i in selected_unit.skills:
                ret = i.button.check_click(event.pos)
                if ret:
                    clicked = True
        if not clicked:
            click_obj(None)
    pass

def click_obj(i: Optional[Entity]):
    global selected_unit, state
    if state is State.NoPlayer or state is State.PlayerSelected:
        selected_unit = i
        if i is None:
            state = State.NoPlayer
    print('unit selected: ', selected_unit)
    if selected_unit is not None and state is State.NoPlayer:
        state = State.PlayerSelected
    pass

def click_sk(i: int):
    global state
    target: Skill = selected_unit.skills[i]
    if state is State.PlayerSelected:
        state = State.SkillSelected

    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):

    fight_background.draw(screen, 0, 0)
    if not (state is State.NoPlayer or state is State.EnemyTurn) and isinstance(selected_unit, Player):
        skills_num = selected_unit.skills
        for j in range(len(skills_num)):
            skills_num[j].button.draw(screen)
            skills_num[j].image.draw(screen, get_x(j, skills_num), 1080-256+35*(256/96), is_center=True)

    if state is State.PlayerSelected:
        if isinstance(selected_unit, Player):
            x = fight_data.ally.index(selected_unit)*150+200
        else:
            x = fight_data.enemy.index(selected_unit)*150+1270
        unit_select.draw(screen, x, 600, is_center=True)
    for i in range(len(ally_button)):
        if ally_button[i] is not None:
            ally_button[i].draw(screen)
    for i in range(len(enemy_button)):
        if enemy_button[i] is not None:
            enemy_button[i].draw(screen)


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