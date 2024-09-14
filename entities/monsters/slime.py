from managers.Entities import Monster
from util.FightData import FightData


class Slime(Monster):
    def action(self, fight_data: FightData):
        fight_data.ally[-1].damage(self.atk)
