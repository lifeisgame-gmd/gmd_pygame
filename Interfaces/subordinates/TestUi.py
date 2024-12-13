import pygame.event

from Interfaces.interface import Interface
from SceneManager import SceneManager
from managers import MapManager
from util.Util import Image


class TestUi(Interface):
    def draw(self, screen):
        self.plate.draw(screen, 960, 540, is_center=True)
        self.button.draw(screen)
        for i in range(len(self.texts)):
            screen.blit(self.texts[i], self.texts[i].get_rect(center=(960, 540)))
        pass

    def __init__(self, text: str, manager: SceneManager):
        self.button = Image('assets/UI/button.png').button(960, 700, lambda: self.button_click(), is_center=True)
        self.plate = Image('assets/UI/setting.png').subsurface(128, 0, 128, 144).scale(384, 432)
        self.font_size = 20
        game_font = pygame.font.Font(r"assets/font/neodgm_code/neodgm_code.ttf", self.font_size) #(r<<<<필수임진짜로없으면경로안불러와지니제발넣어줘"경로/글꼴", 크기) #텍스트에 쓸 글꼴 설정
        self.texts = [game_font.render(i, True, (0, 0, 0)) for i in text.splitlines()]
        self.manager = manager

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.button.check_click(event.pos)

    def button_click(self):
        self.manager.change_scene('map')
        MapManager.cur += 1
        self.deactivate()
        pass
