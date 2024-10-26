from managers.Entities import Monster
from util.FightData import FightData


class LivingArmor(Monster):
    def __init__(self):
        super().__init__("리빙아머", "assets/player/loli", 150, 15)

    def action(self, fight_data: FightData):
        pass