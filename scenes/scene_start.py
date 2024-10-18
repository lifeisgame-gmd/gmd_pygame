import pygame
from util.Button import Button
from util.FightData import FightData
from util.PlayerData import PlayerData


def setup(scene_manager):
    global manager
    global background
    global logo
    global start_button

    manager = scene_manager

    background = pygame.image.load("assets/start/background.jpeg")
    background = pygame.transform.scale(background, (1920, 1080))
    logo = pygame.image.load("assets/start/logo.png")
    logo = pygame.transform.scale(logo, (500, 500))

    from util.Util import Image
    start_button = Image("assets/UI/buttons.png").subsurface(0, 32, 96, 32).scale(300, 100).button(on_click=lambda: manager.change_scene('town'), x=960, y=540, is_center=True)


def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        start_button.check_click(event.pos)

def update():
    pass

def draw(screen):
    screen.blit(background, (0, 0))
    start_button.draw(screen)
    screen.blit(logo, (710, 50))

def cleanup():
    pass
