import pygame
import importlib

class SceneManager:
    def __init__(self):
        self.current_scene = 1
        self.scene_module = None
        self.load_scene(self.current_scene)

    def load_scene(self, scene_number):
        if self.scene_module:
            self.scene_module.cleanup()  # 이전 Scene 정리
        self.scene_module = importlib.import_module(f'scene_{scene_number}')
        self.scene_module.setup(self)  # SceneManager 인스턴스를 전달

    def change_scene(self, scene_number):
        self.current_scene = scene_number
        self.load_scene(scene_number)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.scene_module.handle_event(event)

            self.scene_module.update()
            self.scene_module.draw()
            pygame.display.flip()

scene_manager = SceneManager()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    scene_manager.run()
    pygame.quit()
