import pygame

from Interfaces.interface import Interface
from SceneManager import SceneManager
from util.Util import Image




class FightEnd(Interface):
    def __init__(self, scene_manager: SceneManager):
        global manager, plate,button
        manager = scene_manager
        button = (Image('assets/UI/button.png')
                .scale(192, 64)
                .button(960, 680, lambda: self.button_click(), is_center=True))
        plate = Image('assets/UI/setting.png').subsurface(128, 0, 128, 144).scale(384, 432)

    def draw(self, screen):
        plate.draw(screen, 960, 540, is_center=True)
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