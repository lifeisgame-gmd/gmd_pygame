import pygame
from pygame.locals import *

"""
Town Scene
"""

def setup(scene_manager):
    global color
    global manager
    manager = scene_manager
    color = Color(0, 255, 0)

def handle_event(event):
    pass

def update():
    pass

def draw(screen):
    screen.fill(color)

def cleanup():
    pass
