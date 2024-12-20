from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class HolyKnight(Player):

    def __init__(self):
        super().__init__('성기사',"assets/player/holy_knight.png", 2, 12, 2)
        self.protect += 3
        self.original_protect = self.protect
        self.buff_time = None

    def buff(self, fight_data, additional_data):
        if self.buff_time is None:
          self.buff_time = fight_data.turn + 3
        
          self.protect += self.hp_m * (3/10) 
          return "성기사의 방어력이 증가했다!"
        else:
          self.buff_time += fight_data.turn +3 #버프 중첩 막는 용도. 한 번 더 사용했을때 버프 시간만 늘어남.
    
    def ally_defend(self, fight_data, additional_data : Entity):
        additional_data.protect += self.hp_m * (2/10)
        return "성기사의 방어력이 "+ self.hp_m * (2/10)+  "만큼 증가했다!"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!" 

    skills = [
        Skill('holyknight_atk', '공격', '지정한 적을 공격합니다.', "assets/fight/card1.jpg", attack, Need.Enemy),
        Skill('holyknight_guard', '수호', '지정한 아군에게 보호막 증가.', "assets/player/no_img.png", ally_defend, Need.Ally),
        Skill('holyknight_buff', '신의 방패', '방어 증가.', "assets/fight/card1.jpg", buff, Need.Self)
    ]

    def turn(self, fight_data):
        if self.buff_time == fight_data.turn:
            self.protect = self.original_protect
            self.buff_time = None
        pass