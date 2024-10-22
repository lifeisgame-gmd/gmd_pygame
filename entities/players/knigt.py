from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class Knight(Player):

    def __init__(self):
        super().__init__('기사',"assets/player/cat.png", 10, 4, 1)


    def defend(self, fight_data, additional_data):
        self.protect += 10
        return "기사의 방어력이 10 증가했다!"

    def defend(self, fight_data, additional_data):# 도발 스킬로 
        self.protect += 10                           #다음턴의 적이 주는 데미지를 모두 이 케릭터가 받음.
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('Knight_all_def', '도발', '다음턴의 공격을 모두 자신이 받습니다.', "assets/fight/card1.jpg", defend, Need.Self),
        Skill('Knight_def', '막기', '방패로 막아 방어합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]

    def turn(self, fight_data):
        






        