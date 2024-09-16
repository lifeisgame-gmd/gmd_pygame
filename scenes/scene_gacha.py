import pygame
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

    manager = scene_manager
    background = pygame.image.load("assets/gacha/gacha_background.png") #배경
    background = pygame.transform.scale(background, (1920, 1080))
    Button_image = pygame.image.load("assets/button.png")
    Button_image = pygame.transform.scale(Button_image, (300, 100))
    back_button = Button(Button_image, on_click=lambda: manager.change_scene('town'), x=150, y=650)


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
    back_button.draw(screen)
    pass

# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
