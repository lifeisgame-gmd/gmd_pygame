import random

import pygame

from managers import Player
from managers.EntityManager import PlayerManager
from managers.MapManager import MapManager
from util.Button import Button
from util.PlayerData import PlayerData
from util.Util import Image

"""
Example Scene
"""

# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager):
    global manager
    global background
    global recruitment_button
    global back_button
    global greeting_text
    global gacha_result
    global game_font

    gacha_result = None
    manager = scene_manager
    background = pygame.image.load("assets/gacha/gacha_background.png") #배경
    background = pygame.transform.scale(background, (1920, 1080))
    Button_image = pygame.image.load("assets/button.png")
    Button_image = pygame.transform.scale(Button_image, (300, 100))
    back_button = Button(Button_image, on_click=lambda: manager.change_scene('town'), x=1750, y=1010, is_center=True)
    recruitment_button = Button(Button_image, on_click=lambda: gacha(), x=1000, y=500, is_center=True)

    #폰트 / 글자
    game_font = pygame.font.Font(r"assets/font/빛의 계승자 Regular/HeirofLightRegular.ttf", 100)
    greeting_text = game_font.render("여관", True,(0,0,0)) #("텍스트",안티에일어싱 여부,(R,G,B) 또는 색깔 대문자로 써 넣기.)

    render_text()
    render_party()

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    global party_button
    if event.type == pygame.MOUSEBUTTONDOWN:
        back_button.check_click(event.pos)
        recruitment_button.check_click(event.pos)
        for e in party_button:
            e.check_click(event.pos)
    if event.type == pygame.MOUSEMOTION:
        global mouse_pos
        mouse_pos = event.pos

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    global gacha_result, text_ui, gold_usage, party_button
    screen.blit(background,(0,0))
    back_button.draw(screen)
    recruitment_button.draw(screen)
    screen.blit(greeting_text,(0,0))
    pygame.draw.rect(screen, (255,255,255),[10, 150, 500, 800]) #사각형 그리기 / 설명창
    pygame.draw.ellipse(screen, (0,0,255),[760,100,500,300]) #타원 그리기 / 대충 몬스터 그려봄 ㅇㅇ.
    pygame.draw.rect(screen, (255,255,255),[1450, 10, 450, 100]) #돈/ 재화 띄우는 곳
    for i in range(4):
        pygame.draw.rect(screen, (255,255,255),[740 + 110*i, 700, 100, 100], 2) #돈/ 재화 띄우는 곳
    for e in party_button:
        e.draw(screen)
    screen.blit(text_ui,(1450,10))
    screen.blit(gold_usage, (1000, 500))
    if gacha_result is not None:
        image: Image = gacha_result.image
        image.scale(128, 128).draw(screen, 1010, 250, True)

    pass

# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass

def gacha():
    if PlayerData.gold < 10:
        return
    PlayerData.gold -= 10
    render_text()
    st = 1
    for i in range(MapManager.cur):
        if MapManager.map_data['map'][i] == "T":
            st += 1
    from typing import List
    target: List[Player] = []
    for key, player in PlayerManager.arr.items():
        if player.rank <= st:
            target.append(player)
    global gacha_result
    gacha_result = target[random.randint(0, len(target) - 1)]

def render_text():
    global text_ui, gold_usage
    game_font = pygame.font.Font(r"assets/font/빛의 계승자 Regular/HeirofLightRegular.ttf", 100)
    text_ui = game_font.render(str(PlayerData.gold)+" GOLD", True,(0,0,0))
    gold_usage = game_font.render("-10 G", True,(0,0,0))

def render_party():
    global party_button

    party_button = []

    i = 0
    for e in PlayerData.party:
        i += 1
        party_button.append(e.image.scale(100, 100).button(630 + 110*i, 700, lambda: button_click()))

def button_click():
    global mouse_pos, gacha_result
    i: int = (mouse_pos[0] - 600)/100
    if gacha_result is not None:
        PlayerData.party[i] = gacha_result
        gacha_result = None
    render_party()
