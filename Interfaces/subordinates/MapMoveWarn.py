import pygame.font
from pygame import MOUSEBUTTONDOWN

from Interfaces.interface import Interface
from SceneManager import SceneManager
from util.Util import Image


class MapMoveWarn(Interface):
    def draw(self, screen):
        self.plate.draw(screen, 960, 540, True)
        screen.blit(self.message, (100, 600))
        self.map_button.draw(screen)
        self.town_button.draw(screen)


    def __init__(self, manager: SceneManager):
        self.map_button = Image("assets/UI/mark_O.png").button(1060, 700, lambda: manager.change_scene("map"), True)
        self.town_button = Image("assets/UI/mark_X.png").button(860, 700, lambda: self.deactivate(), True)
        self.plate = Image('assets/UI/setting.png').subsurface(128, 0, 128, 144).scale(384, 432)
        game_font = pygame.font.Font(r"assets/font/neodgm_code/neodgm_code.ttf", 20)
        self.message = game_font.render("파티에 구성원이 없습니다! 정말 진행하시겠습니까?", True, (0, 0, 0))
        pass

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.map_button.check_click(event.pos)
            self.town_button.check_click(event.pos)
        pass