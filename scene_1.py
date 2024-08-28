import pygame

"""
Start Scene
"""


def setup(scene_manager):
    global color
    global manager
    manager = scene_manager

def handle_event(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_2:
            manager.change_scene(2)

def update():
    pass

def draw(screen):
    screen.fill(color)

def cleanup():
    pass
