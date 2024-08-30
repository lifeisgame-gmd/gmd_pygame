import pygame
from pygame.locals import *
import Util

"""
Start Scene
"""


def setup(scene_manager):
    global manager
    global background
    global button
    global logo

    manager = scene_manager


    # 이미지 파일들을 불러옵니다.
    background = pygame.image.load("assets/background.jpeg")
    background = pygame.transform.scale(background, (1920, 1080))
    button = pygame.image.load("assets/Buttons.png").subsurface((0, 32, 96, 32))
    button = pygame.transform.scale(button, (480, 160))
    logo = pygame.image.load("assets/logo.png")
    logo = pygame.transform.scale(logo, (500, 500))
    

def handle_event(event):
    if event.type == pygame.KEYDOWN: # 키를 눌렀다면
        if event.key == pygame.K_2: # 이벤트의 키가 2번 키라면
            manager.change_scene('sans') # sans 씬으로 넘어갑니다.
    if event.type == pygame.MOUSEBUTTONDOWN: # 마우스 왼쪽 버튼을 눌렀다면
        if Util.collide(720, 540, 480, 160): # 버튼 안에 있는지를 감지합니다. 곧 수정될 메소드입니다.
            manager.change_scene('sans') # 버튼 안에서 왼쪽 버튼을 눌렀다면, sans 씬으로 넘어갑니다.

def update():
    pass

def draw(screen):

    #버튼들을 그립니다.
    screen.blit(background, (0, 0))
    screen.blit(button, (720, 540))
    screen.blit(logo, (710, 50))
    

def cleanup():
    pass
