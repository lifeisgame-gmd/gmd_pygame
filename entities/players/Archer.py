import random
from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class Archer(Player):

    def __init__(self):
        super().__init__('궁수',"assets/player/Archer.png", 70, 30, 2)
        self.protect += 3
        self.current_turn = 0
        self.buff_time = 0


    def attack(self, fight_data, additional_data):
        additional_data.damage(20)
        additional_data.damage(20)
        additional_data.damage(20)
        return additional_data.name + "을(를) 20의 데미지로 공격했다!" + "\n" + additional_data.name+ "을(를) 20의 데미지로 공격했다!"  + "\n" + additional_data.name+ "을(를) 20의 데미지로 공격했다!"

    def attention(self, fight_data:FightData, additional_data : Entity):
        pass


    def buff(self, fight_data, additional_data):
        self.protect += self.hp_m * (15/100)
        return "궁수의 방어력이 증가했다!"

    def shield(self, fight_data, additional_data):
        self.buff_time = fight_data.turn + 1
        return "다음 1턴 동안 30%의 확률로 공격을 상쇄한다!"

    def damage(self, atk):
        if self.buff_time < self.current_turn:
            if random.randrange(1, 100) > 30:
                super().damage(atk)
                

    def turn(self, fight_data):
        self.current_turn = fight_data.turn


    skills = [
        Skill('Archer_atk', '고속 연사', '지정한 적을 3개의 화살로 공격합니다.', "assets/fight/card1.jpg", attack, Need.Enemy),
        Skill('Archer_buff', '방어', '해당 캐릭터의 방어력을 높입니다.', "assets/player/no_img.png", buff, Need.Self),
        Skill('Archer_shield', '공격방어', '30%의 확률로 적의 공격을 상쇄합니다.', "assets/player/no_img.png", shield, Need.Self)
]

        
