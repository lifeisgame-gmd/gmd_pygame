import pygame

from Interfaces.interface import Interface
from SceneManager import SceneManager
from util.Util import Image




class FightEnd(Interface):
    def __init__(self, scene_manager: SceneManager):
        global button
        global manager
        manager = scene_manager
        button = Image('assets/UI/button.png').button(960, 540, lambda: self.button_click(), is_center=True)

    def draw(self, screen):
        button.draw(screen)
        pass

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.check_click(event.pos)
            self.deactivate()

    def button_click(self):
        manager.change_scene('map')
        from managers.MapManager import MapManager
        MapManager.cur += 1