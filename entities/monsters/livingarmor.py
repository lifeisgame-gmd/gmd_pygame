import random
from typing import Optional

from audioop import reverse

from managers import Player
from managers.Entities import Monster
from util.FightData import FightData


class LivingArmor(Monster):
    def __init__(self):
        super().__init__("리빙아머", "assets/player/loli.png", 150, 15)

    def action(self, fight_data: FightData):
        rand = random.randrange(1, 10)
        if(rand == 1):
            self.protect += 1
            return "리빙아머의 방어력이 1 상승했다!"
        else:
            e : Optional[Player]
            for e in reverse(fight_data.ally):
                if e is None:
                    continue
                e.damage(self.atk)
                return e.name+"을(를) "+self.atk+"의 데미지로 공격했다!"