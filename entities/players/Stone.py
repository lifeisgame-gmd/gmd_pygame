from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need

class Stone(Player):


    def __init__(self):
        super().__init__('돌맹이',"assets/player/dog.png", 4, 35, 1) # 이름, 사진 경로, 공격력, 체력, 1


    def defend(self, fight_data: FightData, additional_data: Entity):
        self.protect += 10
        return "돌맹이는 단단해져 방어력이 10 증가했다!"

    def punch(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(10)
        return "적군이 돌맹이를 밟고 넘어져 10의 데미지를 받았다"
        
    skills = [
        Skill('stone_atk', '가만히 있기' ,'지정한 적이 돌맹이를 밟습니다.', 'assets/fight/card1/jpg', punch, Need.Enemy), #Need - Enemy, Ally, Self, Any
        Skill('stone_def', '돌맹이는 단단해', '단단합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]


# "assets/player/no_img.png"
