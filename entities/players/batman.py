from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need

class Batman(Player):
    

    def __init__(self):
        super().__init__('배트맨',"assets/player/dog.png", 15, 10, 1) # 이름, 사진 경로, 공격력, 체력, 1


    def punch(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(10)
        return "배트맨이 적군을 10의 데미지로 공격했다"
        
    skills = [
        Skill('dog_punch', '방망이 휘두르기' ,'지정한 적에게 방망이를 휘둘러 공격합니다.', 'assets/fight/card1/jpg', punch, Need.Enemy) #Need - Enemy, Ally, Self, Any
    ]


# "assets/player/no_img.png"
