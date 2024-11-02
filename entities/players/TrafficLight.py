from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need

class TrafficLight(Player):

    def __init__(self):
        super().__init__('신호등',"assets/player/shd.png", 10, 4)


    def defend(self, fight_data, additional_data):
        self.defend += 5
        return "신호등의 방어력이 5 증가했다!"

    def stun_sk(self, fight_data: FightData, additional_data):
        additional_data.stun(self.atk)      #스턴!!        #스턴 넣기!!!!!
        return "신호가 빨간불이 되었다!"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('TrafficLight_atk', '초록불', '지정한 적을 공격합니다.', "assets/fight/card1.jpg", attack, Need.Enemy),
        Skill('TrafficLight_cc', '정지', '빨간불이 되어 상대가 다음 신호를 기다립니다.', "assets/player/no_img.png", attack, Need.Enemy), #지정한 한명 스턴넣기
        Skill('TrafficLight_def', '빨간불', '정지하여 자신을 보호합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]

