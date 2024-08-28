import importlib

import pygame


class SceneManager:
    def __init__(self):
        self.current_scene = 1
        self.scene_module = None
        self.load_scene(self.current_scene)

        self.base_width = 1920
        self.base_height = 1080
        self.virtual_screen = None
        self.scale = 1.0
        self.update_virtual_screen()

    def update_virtual_screen(self):
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h

        scale_x = screen_width / self.base_width
        scale_y = screen_height / self.base_height
        self.scale = min(scale_x, scale_y)

        virtual_width = int(self.base_width * self.scale)
        virtual_height = int(self.base_height * self.scale)
        self.virtual_screen = pygame.Surface((virtual_width, virtual_height))

    def load_scene(self, scene_number):
        if self.scene_module:
            self.scene_module.cleanup()
        self.scene_module = importlib.import_module(f'scene_{scene_number}')
        self.scene_module.setup(self)

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

            self.virtual_screen.fill((0, 0, 0))
            self.scene_module.draw(self.virtual_screen)

            scaled_screen = pygame.transform.scale(self.virtual_screen, (pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height()))
            pygame.display.get_surface().blit(scaled_screen, (0, 0))
            pygame.display.flip()
