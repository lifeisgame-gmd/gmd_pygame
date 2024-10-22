from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need

class Star(Player):
    

    def __init__(self):
        super().__init__('오각별',"assets/player/cat.png", 10, 4) # 이름, 캐릭터 사진, 공격력, 체력, 1

    def starpower(self, fight_data: FightData, additional_data: Entity):
        additional_data.hp_c = 0
        return "오각별이 지정한 적을 죽였습니다!"

    skills = [
        Skill('star_starpower', '별별 파워!', '지정한 적을 죽입니다.', 'assets/player/no_img.png',starpower, Need.Enemy) # Enemy, Ally, Self, Any
    ]