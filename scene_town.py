import pygame
from Button import Button
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
    manager = scene_manager

    #이미지 불러오기
    background = pygame.image.load("assets/village_background.png") #배경
    background = pygame.transform.scale(background, (1920, 1080))
    request_office_image = pygame.image.load("assets/request_office.png")
    request_office_image = pygame.transform.scale(request_office_image, (300, 500))
    request_office = Button(request_office_image, on_click=lambda: manager.change_scene('quset'), x=250, y=650)
    smithy_image = pygame.image.load("assets/smithy.png") #대장간 / 강화소
    smithy_image = pygame.transform.scale(smithy_image, (300, 500))
    smithy = Button(smithy_image, on_click=lambda: manager.change_scene('upgrade'), x=650, y=650)
    hotel_image = pygame.image.load("assets/hotel.png") #여관 / 치료소
    hotel_image = pygame.transform.scale(hotel_image, (300, 500))
    hotel = Button(hotel_image, on_click=lambda: manager.change_scene('hotel'), x=1050, y=650)

    
# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event): 
    if event.type == pygame.MOUSEBUTTONDOWN:
        request_office.check_click(event.pos)
        smithy.check_click(event.pos)
        hotel.check_click(event.pos)
     
    pass    

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    screen.blit(background, (0, 0))
    request_office.draw(screen)
    smithy.draw(screen)
    hotel.draw(screen)
    pass

# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
