import pygame
from Util import Image
"""
Town Scene
"""

# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager):
    global manager
    global background
    global request_office
    global smithy
    global hotel
    global to_map
    manager = scene_manager

    #이미지 불러오기
    background = Image("assets/town/village_background.png").scale(1920, 1080) # 배경
    request_office = Image("assets/town/request_office.png").scale(300, 500).button(250, 650, lambda: manager.change_scene('quest')) # 의뢰소
    smithy = Image("assets/town/smithy.png").scale(300, 500).button(650, 650, lambda: manager.change_scene('upgrade')) #대장간 / 강화소
    hotel = Image("assets/town/hotel.png").scale(300, 500).button(1050, 650, lambda: manager.change_scene('hotel')) #여관 / 치료소
    to_map = Image("assets/town/map.png").scale(300, 300).button(1620, 200, lambda: manager.change_scene('map'))


    
# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event): 
    if event.type == pygame.MOUSEBUTTONDOWN:
        request_office.check_click(event.pos)
        smithy.check_click(event.pos)
        hotel.check_click(event.pos)
        to_map.check_click(event.pos)

    pass    

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    background.draw(screen, 0, 0)
    request_office.draw(screen)
    smithy.draw(screen)
    hotel.draw(screen)
    to_map.draw(screen)
    pass

# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
