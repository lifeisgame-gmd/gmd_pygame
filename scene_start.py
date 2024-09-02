import pygame
from pygame.locals import *
import Util

# Button 클래스를 import합니다.
from Button import Button  # Button 클래스가 정의된 파일을 import

def setup(scene_manager):
    global manager
    global background
    global logo
    global start_button

    manager = scene_manager

    # 이미지 파일들을 불러옵니다.
    background = pygame.image.load("assets/background.jpeg")
    background = pygame.transform.scale(background, (1920, 1080))
    logo = pygame.image.load("assets/logo.png")
    logo = pygame.transform.scale(logo, (500, 500))

    # 버튼을 생성합니다. 중앙에 배치되도록 x, y를 설정합니다.
    button_image = pygame.image.load("assets/Buttons.png").subsurface((0, 32, 96, 32))
    start_button = Button(button_image, on_click=lambda: manager.change_scene('town'), x=960, y=540)  # 중앙 위치

def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 왼쪽 버튼을 눌렀다면
        start_button.check_click(event.pos)  # 버튼 클릭 감지

def update():
    pass

def draw(screen):
    # 버튼들을 그립니다.
    screen.blit(background, (0, 0))
    start_button.draw(screen)  # 버튼 그리기
    screen.blit(logo, (710, 50))

def cleanup():
    pass
