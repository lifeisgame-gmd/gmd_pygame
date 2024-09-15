from typing import Callable, Dict, Any, List

from util.FightData import FightData


class Skill:
    def __init__(self, sk_id, name, desc, src, on_enable: Callable[[FightData, Dict[str, Any]], None], need_data: List[str]):
        self.on_enable = on_enable
        self.name = name
        self.desc = desc
        self.src = src
        self.id = sk_id
        self.need_data = need_data

    def activate(self, fight_data: FightData, additional_data: Dict[str, Any]):
        self.on_enable(fight_data, additional_data)
