import pygame

"""
Example Scene
"""

# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager):
    global manager
    global background
    global quest_text #텍스트 가로-1920, 세로 - 1080
    global quest_1
    global quest_2
    global quest_3
    manager = scene_manager

    background = pygame.image.load("assets/background.jpeg") #배경
    background = pygame.transform.scale(background, (1920, 1080))
    quest_text_image = pygame.image.load("assets/hotel.png")#
    quest_text = pygame.transform.scale(quest_text_image, (400, 800))
    quest_1_image = pygame.image.load("assets/smithy.png")#
    quest_1 = pygame.transform.scale(quest_1_image, (300, 500))
    quest_2_image = pygame.image.load("assets/smithy.png")#
    quest_2 = pygame.transform.scale(quest_2_image, (300, 500))
    quest_3_image = pygame.image.load("assets/smithy.png")#
    quest_3 = pygame.transform.scale(quest_3_image, (300, 500))

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    screen.blit(background, (0, 0))
    screen.blit(quest_text, (50, 50))
    screen.blit(quest_1, (500, 100))
    screen.blit(quest_2, (700, 100))
    screen.blit(quest_3, (1000, 100))

# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
