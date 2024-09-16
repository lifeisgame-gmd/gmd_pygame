from enum import Enum
from typing import Callable, Dict, Any, List

from managers.Entities import Entity
from util.FightData import FightData

class Need(Enum):
    Self = 0
    Ally = 1
    Enemy = 2
    Any = 3

class Skill:
    def __init__(self, sk_id, name, desc, src, on_enable: Callable[[Entity, FightData, Entity], None], need_data: Need):
        self.on_enable = on_enable
        self.name = name
        self.desc = desc
        self.src = src
        self.id = sk_id
        self.need_data = need_data

    def activate(self, entity_self,  fight_data, additional_data):
        return self.on_enable(entity_self, fight_data, additional_data)
