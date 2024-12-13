from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need

class Dog(Player):


    def __init__(self):
        super().__init__('강아지',"assets/player/dog.png", 10, 4, 1) # 이름, 사진 경로, 공격력, 체력, 1


    def punch(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(10)
        return "멍멍이가 적군을 10의 데미지로 공격했다"
        
    skills = [
        Skill('dog_punch', '멍멍 펀치!' ,'지정한 적을 공격합니다.', 'assets/fight/card1.jpg', punch, Need.Enemy) #Need - Enemy, Ally, Self, Any
    ]


# "assets/player/no_img.png"
