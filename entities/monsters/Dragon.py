from typing import Optional

from managers import Monster, Player
from util.FightData import FightData


class SkeletonArcher(Monster):
    def __init__(self):
        super().__init__("드래곤", "assets/player/loli.png", 100, 250)

    def action(self, fight_data: FightData):
        for i in reversed(range(len(fight_data.ally))):
            if fight_data.ally[i] is None:
                continue
            fight_data[i].damage(self.atk)
            if i > 1 and fight_data[i-1] is not None:
                fight_data[i-1].damage(self.atk)
             
            if fight_data.ally[i-1] is None:
                return "드레곤이 브레스를 뿜어서 " + fight_data[i].name +"에게 "+ str(self.atk)+"데미지를 줬다"
            else:
                return "드레곤이 브레스를 뿜어서 " + fight_data[i].name +", "+ fight_data[i-1].name +"에게 "+ str(self.atk)+"데미지를 줬다"
        else:
            e : Optional[Player]
            for e in reverse(fight_data.ally):
                if e is None:
                    continue
                e.damage(self.atk)
                return e.name+"을(를) "+self.atk+"의 데미지로 공격했다!"


        return "드레곤이 브레스를 뿜어 " + str(self.atk)+ " 데미지를 줬다"
       