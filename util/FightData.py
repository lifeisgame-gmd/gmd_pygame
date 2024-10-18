from collections import OrderedDict
from typing import List, Any, Optional
import json

from managers.Entities import Player, Monster


class FightData:
    def __init__(self,ally: List[Optional['Player']],  enemy: List[Optional['Monster']]):
        self.ally = ally
        self.enemy = enemy
        self.turn = 0

    def __str__(self):
        data = OrderedDict()
        data['players'] = [player.name for player in self.ally if player is not None]
        data['enemies'] = [monster.name for monster in self.enemy if monster is not None]
        return json.dumps(data)