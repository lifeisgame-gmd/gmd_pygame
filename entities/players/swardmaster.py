from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class samurai(Player):

    def __init__(self):
        super().__init__('검사',"assets/player/cat.png", 7, 5)


    def punch(self, fight_data: FightData, additional_data: Entity):
    additional_data.damage(7)
    return "검사가 적군을 7의 데미지로 공격했다"

    def attack(self, fight_data: FightData, additional_data: Entity):
        for samu_atk in range(3):
        additional_data.damage(self.atk)
        break
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 3번 공격했다!"

    skills = [
        Skill('cat_atk', '빠르게 베기', '지정한 적을 빠르게 베어 공격합니다.', "assets/player/loli.jpg", attack, Need.Enemy),
        Skill('cat_def', '3연 베기', '적을 3번 연속 베어 공격합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]

