import pygame
from util.Util import Image
from util.Button import Button

"""
Example Scene
"""

# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager):
    global manager
    global background
    global platform
    global character
    global upgrade
    global back_button
    manager = scene_manager

    #이미지 불러오기
    background = Image("assets/upgrade/background.jpg").scale(1920, 1080) # 배경
    character = Image("assets/upgrade/character.png").scale(800, 800) #캐릭터 전시 화면
    platform = Image("assets/upgrade/platform.png").scale(350, 80) #강화대(원판)
    upgrade = Image("assets/upgrade/upgrade.png").scale(450, 450) #스탯 업
    Button_image = pygame.image.load("assets/button.png")
    Button_image = pygame.transform.scale(Button_image, (300, 100))
    back_button = Button(Button_image, on_click=lambda: manager.change_scene('town'), x=1750, y=1010, is_center=True)

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
    background.draw(screen, 0, 0)
    character.draw(screen, 1000, 100)
    platform.draw(screen, 250, 450)
    upgrade.draw(screen, 200, 550)
    back_button.draw(screen)
    back_button.draw(screen)
# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
