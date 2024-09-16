import pygame
import ctypes

u32 = ctypes.windll.user32
resolution = u32.GetSystemMetrics(0), u32.GetSystemMetrics(1)

from SceneManager import SceneManager



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(resolution,pygame.FULLSCREEN)  # 창 크기 조절 가능
    scene_manager = SceneManager(screen)
    scene_manager.run()
    pygame.quit()
