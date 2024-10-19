import random
from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need

class Wizard(Player):


    def __init__(self):
        super().__init__('마법사',"assets/player/Wizard.png", 60, 20, 1) # 이름, 사진 경로, 공격력, 체력, 1


    def fireattack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(60)
        return "마법사가 적군을 60의 데미지로 공격했다!"

    def iceattack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(40)
        return "마법사가 적군을 40의 데미지로 공격했다!"


    def defend(self, fight_data: FightData, additional_data: Entity):
        additional_data.protect += 15
        return "아군의 방어력이 15 증가했다!"

    def recovery(self, fight_data: FightData, additional_data: Entity):
        additional_data.hp_c = min(additional_data.hp_c + 10, additional_data.hp_m)
        return "마법사의 체력이 10 회복됐다!"
        
    skills = [
        Skill('Wizard_fireattack', '파이어 볼!' ,'지정한 적을 공격합니다.', 'assets/fight/card1/jpg', fireattack, Need.Enemy)
        Skill('Wizard_fireattack', '아이스 볼!' ,'지정한 적을 공격합니다.', 'assets/fight/card1/jpg', iceattack, Need.Enemy)  #Need - Enemy, Ally, Self, Any
        Skill('Wizard_defend', '쉴드!', '방어벽을 전개합니다.', 'assets/player/no_img.png', defend, Need.Ally)
        Skill('Wizrad_recovery', '회복!', '체력을 회복합니다.', 'assets/player/no_img.png', recovery, Need.Self)
    ]


# "assets/player/no_img.png"
