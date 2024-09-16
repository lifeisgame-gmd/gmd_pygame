import pygame

from SceneManager import SceneManager



if __name__ == "__main__":
    pygame.init()

    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.NOFRAME)
    virtual_screen = pygame.Surface((1920, 1080))
    scene_manager = SceneManager(screen, virtual_screen)
    scene_manager.run()
    pygame.quit()
