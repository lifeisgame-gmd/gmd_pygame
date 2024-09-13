import pygame

"""
Example Scene
"""

# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager):
    global manager
    manager = scene_manager
    global fight_background
    global fight_skill_card
    global fight_skill_card2
    fight_background = pygame.image.load("assets/fight/fight_bg.jpg")
    fight_background = pygame.transform.scale(fight_background, (1920, 1080))
    fight_skill_card=pygame.image.load("assets/fight/card1.jpg")
    fight_skill_card2=pygame.image.load("assets/fight/card2.jpg")

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    screen.blit(fight_background, (0, 0))
    screen.blit(fight_skill_card, (960,780))
    screen.blit(fight_skill_card2, (830,780))

# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
