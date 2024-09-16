from managers.Entities import Monster
from util.FightData import FightData


class Slime(Monster):

    def __init__(self):
        super().__init__("슬라임", "assets/monster/slime.png", 10, 1)

    def action(self, fight_data: FightData):

        target = next((item for item in reversed(fight_data.ally) if item is not None), None)
        target.damage(self.atk)
        return target.name + "을(를) " + str(self.atk) + "의 데미지로 공격했다!"
