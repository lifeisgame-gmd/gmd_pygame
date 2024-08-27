import pygame

def setup(scene_manager):
    global color
    global manager
    manager = scene_manager  # SceneManager 인스턴스 저장
    color = (0, 0, 255)  # 파란색

def handle_event(event):
    if event.type == pygame.KEYDOWN:
        print(f'Key pressed in Scene 2: {event.key}')
        if event.key == pygame.K_1:
            manager.change_scene(1)

def update():
    pass

def draw():
    screen = pygame.display.get_surface()
    screen.fill(color)

def cleanup():
    pass
