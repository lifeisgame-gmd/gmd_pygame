from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class MyakMyak(Player):

    def __init__(self):
        super().__init__('먁먁',"assets/player/myakmyak.png", 2, 12, 1000)
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
    
    def Ally_defend(self, fight_data, additional_data : Entity):
        additional_data.protect += self.hp_m * (2/10)
        return "성기사의 방어력이 "+ str(self.hp_m * (2/10))+  "만큼 증가했다!"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!" 

    skills = [
        Skill('ToBeMyak', '먁먁이되', '먁먁, 먁먁먁먁.', "assets/fight/card1.jpg", attack, Need.Enemy),
        Skill('printf("Hello world!");', '안녕 세계!', '콘솔창을 열어 기본 텍스트를 출력해 공격합니다..', "assets/player/no_img.png", Ally_defend, Need.Ally),
        Skill('dreaming', '공상하기', '데미지를 주고, 준 피해량 만큼 회복합니다.', "assets/fight/card1.jpg", buff, Need.Self),
        Skill('miaping', '개큰미아핑', '아주 큰 미아핑이 지정한 적 머리위로 떨어집니다.', "assets/fight/card1.jpg", buff, Need.Self)
    ]

    def turn(self, fight_data):
        if self.buff_time == fight_data.turn:
            self.protect = self.original_protect
            self.buff_time = None
        pass