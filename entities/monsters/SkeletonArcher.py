from typing import Optional

from managers import Monster, Player
from util.FightData import FightData


class SkeletonArcher(Monster):
    def __init__(self):
        super().__init__("스켈레톤 궁수", "assets/player/loli.png", 70, 30)

    def action(self, fight_data: FightData):
        lowest: Optional[Player] = None
        for e in fight_data.ally:
            if lowest is None:
                lowest = e
                continue
            if e.hp_c < lowest.hp_c:
                lowest = e
        lowest.damage(self.atk)
        return lowest.name+"을(를) "+self.atk+"의 데미지로 공격했다!"