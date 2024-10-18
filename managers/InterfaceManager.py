from typing import List
from Interfaces.interface import Interface
from Interfaces.subordinates.fight_end import FightEnd
from SceneManager import SceneManager
from managers.MapManager import MapManager


class UIManager:
    ui_list: dict[str, Interface] = {}
    @staticmethod
    def init(manager):
        UIManager.ui_list['fight_end'] = FightEnd(manager)

    @staticmethod
    def activate(name: str):
        SceneManager.ui = UIManager.ui_list[name]

