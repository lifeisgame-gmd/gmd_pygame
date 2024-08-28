import pygame

"""
Town Scene
"""

def setup(scene_manager):
    global color
    global manager
    manager = scene_manager

def handle_event(event):
    if event.type == pygame.KEYDOWN:
        print(f'Key pressed in Scene 2: {event.key}')
        if event.key == pygame.K_1:
            manager.change_scene(1)

def update():
    pass

def draw(screen):
    screen.fill(color)

def cleanup():
    pass
