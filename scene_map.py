import pygame
import pygame

from Util import Image

"""
Example Scene
"""

# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager):
    global manager
    global background
    manager = scene_manager

    background = Image("assets/map/map_bg.png").scale(1920, 1080)

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    background.draw(screen, 0, 0)

# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
