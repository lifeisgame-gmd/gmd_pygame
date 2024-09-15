from typing import Any

from managers.Entities import Player
from util.FightData import FightData
from util.Skill import Skill


class Cat(Player):


    def defend(self, fight_data, additional_data):
        self.protect += 5

    def attack(self, fight_data: FightData, additional_data: dict[str, Any]):
        additional_data['Enemy'].damage(self.atk)

    skills = [
        Skill('cat_atk', '냥냥 펀치', '지정한 적을 공격합니다.', "assets/player/no_img.png", attack, ['Enemy']),
        Skill('cat_def', '냥냥 방어', '털로 몸을 감싸 방어합니다.', "assets/player/no_img.png", defend, [])
    ]

