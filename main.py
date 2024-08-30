import pygame

from SceneManager import SceneManager



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)  # 창 크기 조절 가능
    scene_manager = SceneManager()
    scene_manager.run()
    pygame.quit()
