from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class Knight(Player):

    def __init__(self):
        super().__init__('성기사',"assets/player/cat.png", 10, 4, 1)


    def defend(self, fight_data, additional_data):
        self.protect += 10
        return "성기사의 방어력이 10 증가했다!"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('Knight_atk', '심판', '지정한 적을 공격합니다.', "assets/fight/card1.jpg", attack, Need.Enemy),#최대체력의 15퍼센트, 2턴 후 부터 사용 가능, 4턴마다 1번씩
        Skill('Knight_def', '막기', '방패로 막아 방어합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]

    def turn(self, fight_data):
        






        