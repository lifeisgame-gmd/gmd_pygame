from Interfaces.interface import Interface
from SceneManager import SceneManager
from util.Util import Image


def button_click():
    manager.change_scene('map')


class FightEnd(Interface):
    def __init__(self, scene_manager: SceneManager):
        global button
        global manager
        manager = scene_manager
        button = Image('assets/UI/button.png').button(960, 540, lambda: button_click(), is_center=True)

    def draw(self, screen):
        pass

