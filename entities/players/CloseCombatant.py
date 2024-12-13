import random
from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need

class CloseCombatant(Player):

    def __init__(self):
        super().__init__('근접전투원', "assets/player/closecombatant.png", 20,65, 2)


    def neckattack(self, fight_data: FightData, additional_data: Entity):
        r = random.randrange(0,71)
        additional_data.damage(self.atk + r)
        return "근접전투원이 적군을" + str(self.atk + r)+"의 데미지로 공격했다!"

    def defend(self, fight_data, additional_data):
        self.protect += 20
        return "근접전투원의 방어력이 20 증가했다!"

    def neckattack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return "근접전투원이 적군을" + str(self.atk)+"의 데미지로 공격했다!"
    

    skills = [
        Skill('closecombantant_atk', '넥슬라이스', '지정한 적의 목을 벱니다.', "assets/fight/card1.jpg", neckattack, Need.Enemy),
        Skill('closecombantant_defend', '집중 방어', '무기를 방패삼아 적의 공격을 방어합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]
