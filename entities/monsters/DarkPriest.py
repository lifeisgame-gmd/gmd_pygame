from typing import Optional

from managers import Monster, Player
from util.FightData import FightData


class DarkPriest(Monster):
    def __init__(self):
        super().__init__("타락 성기사", "assets/player/loli/png", 200, 20)

    def action(self, fight_data: FightData):
        if fight_data.turn % 2 == 0:
            hightest: Optional[Player] = None
            for e in fight_data.ally:
                if e is None:
                    continue
                if hightest is None:
                    hightest = e
                    continue
                if hightest.hp_m < e.hp_m:
                    hightest = e
            hightest.damage(self.atk)
            return hightest.name+"을(를) "+self.atk+"의 데미지로 공격했다!"
        else:
            lowest: Optional[Monster] = None
            for e in fight_data.enemy:
                if e is None:
                    continue
                if lowest is None:
                    lowest = e
                    continue
                if lowest.hp_c > e.hp_c:
                    lowest = e
            lowest.heal(self.atk)
            return lowest.name+"을(를) "+self.atk/2+"만큼 회복시켰다!"