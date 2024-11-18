from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class Cat(Player):

    def __init__(self):
        super().__init__('고양이',"assets/player/cat.png", 10, 1)


    def defend(self, fight_data, additional_data):
        self.protect += 5
        return "고양이의 방어력이 5 증가했다!"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        additional_data.stun(fight_data.turn + 1)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('cat_atk', '냥냥 펀치', '지정한 적을 공격합니다.', "assets/player/loli.jpg", attack, Need.Enemy),
        Skill('cat_def', '냥냥 방어', '털로 몸을 감싸 방어합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]

