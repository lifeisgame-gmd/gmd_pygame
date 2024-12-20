from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class Potioner(Player):

    def __init__(self):
        super().__init__('연금술사',"assets/player/chemical.png", 20, 20, 1)


    def heal_sk(self, fight_data, additional_data: Entity):
        additional_data.hp_c = min(additional_data.hp_c + 10, additional_data.hp_m)
        return "회복의 물약을 사용했다!"

    def defend(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)      #3턴동안 10의 데미지 입히기
        return "독물약을 던졌다!"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('potioner_atk', '고통의 물약', '지정한 적을 공격합니다.', "assets/fight/card1.jpg", attack, Need.Enemy),
        Skill('potioner_poison', '독의 물약', '3턴동안 매 턴마다 적이 데미지를 받습니다.', "assets/player/no_img.png", defend, Need.Enemy),
        Skill('potioner_heal', '회복의 물약', '지정한 팀원을 회복합니다.', "assets/player/no_img.png", heal_sk, Need.Self)
    ]

    def turn(self, fight_data):
        pass
        # do something you want

