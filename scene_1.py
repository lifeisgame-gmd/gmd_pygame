import pygame
from pygame.locals import *
import Util

"""
Start Scene
"""


def setup(scene_manager):
    global color
    global manager
    global background
    global button
    global logo
    
    manager = scene_manager
    color = Color(255, 0, 0)
    background = pygame.image.load("assets/background.jpeg")
    button = pygame.image.load("assets/button.png")
    button = pygame.transform.scale(button, (480, 160))
    logo = pygame.image.load("assets/logo.png")
    logo = pygame.transform.scale(logo, (500, 500))
    

def handle_event(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_2:
            manager.change_scene('sans')
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()    
        if Util.collide(720, 540, 480, 160):
            manager.change_scene('sans')

def update():
    
    pass

def draw(screen):
    screen.blit(background, (0, 0))
    screen.blit(button, (720, 540))
    screen.blit(logo, (710, 50))
    

def cleanup():
    pass
