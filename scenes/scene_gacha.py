import pygame
from util.Button import Button

from SceneManager import SceneManager
from managers.EntityManager import PlayerManager, MonsterManager
from managers.MapManager import MapManager
from util.PlayerData import PlayerData
from util.Button import Button

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
    global Hero_Description

    manager = scene_manager
    background = pygame.image.load("assets/gacha/gacha_background.png") #배경
    background = pygame.transform.scale(background, (1920, 1080))
    Button_image = pygame.image.load("assets/button.png")
    Button_image = pygame.transform.scale(Button_image, (300, 100))
    back_button = Button(Button_image, on_click=lambda: manager.change_scene('town'), x=1750, y=1010, is_center=True)
    Hero_Description = pygame.Rect(0, 0, 300, 1500)

    #폰트 / 글자
    game_font = pygame.font.Font(r"assets\font\빛의 계승자 Regular\HeirofLightRegular.ttf", 100)
    greeting_text = game_font.render("여관.", True,(0,0,0)) #("텍스트",안티에일어싱 여부,(R,G,B) 또는 색깔 대문자로 써 넣기.)

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        back_button.check_click(event.pos)
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    screen.blit(background,(0,0))
    back_button.draw(screen)
    screen.blit(greeting_text,(0,0))
    pygame.draw.rect(screen, (255,255,255),[10, 150, 500, 800])
    pass

# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
