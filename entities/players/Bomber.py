from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class Bomber(Player):

    def __init__(self):
        super().__init__('폭탄병',"assets/player/bomber.png", 10, 10, 2)


    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        for i in range(fight_data.enemy):
            if fight_data.enemy[i] is not additional_data:
                continue
            if i > 1 and fight_data.enemy[i-1] is not None:
                fight_data.enemy[i-1].damage(self.atk)
            fight_data.enemy[i].damage(self.atk)
            if i < 4 and fight_data.enemy[i+1] is not None:
                fight_data.enemy[i+1].damage(self.atk)

        return "폭탄을 던져 적무리에게" + str(self.atk)+ "데미지를 줬다"
       

    def ranged_attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('bomber_atk1', '냥냥 펀치', '지정한 적을 공격합니다.', "assets/player/loli.jpg", attack, Need.Enemy),
        Skill('bomber_atk2', '냥냥 방어', '폭탄들 던져 1명에게 공격력 만큼의 데미지를 준다.', "assets/player/no_img.png", ranged_attack, Need.Enemy)
    ]

