from typing import List
from Interfaces.interface import Interface
from Interfaces.subordinates.fight_end import FightEnd


class UIManager:
    ui_list: dict[str, Interface]
    @staticmethod
    def init(manager):
        UIManager.ui_list['fight_end'] = FightEnd(manager)

    @staticmethod
    def get(name: str) -> Interface:
        return UIManager.ui_list[name]

