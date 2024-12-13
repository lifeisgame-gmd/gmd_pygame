from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class LightningRat(Player):

    def __init__(self):
        super().__init__('전기쥐',"assets/player/rat.png", 10, 10, 2)


    def defend(self, fight_data, additional_data):
        self.protect += 7
        return "꼬리로 자기 자신을 감싸서 방어력 7을 얻었다"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('cat_atk', '??:백만볼트', '백만볼트를 날린다!!', "assets/player/loli.jpg", attack, Need.Enemy),
        Skill('cat_def', '막기', '꼬리로 몸을 감싸 방어합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]

