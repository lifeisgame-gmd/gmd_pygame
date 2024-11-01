from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


<<<<<<< HEAD:entities/players/TrafficLight.py
class TrafficLight(Player):

    def __init__(self):
        super().__init__('신호등',"assets/player/shd.png", 50, 15, 1)
=======
class TrafficLight(Player):

    def __init__(self):
        super().__init__('신호등',"assets/player/shd.png", 10, 4)
>>>>>>> 9209b8c8c7ab7b1dd7ab132ffcd831e97015ec2e:entities/players/TrafficLight.py


    def defend(self, fight_data, additional_data):
        self.defend += 5
        return "신호등의 방어력이 5 증가했다!"

    def stun(self, fight_data: FightData, additional_data):
        additional_data.stun(self.atk)      #스턴!!        #스턴 넣기!!!!!
        return "신호가 빨간불이 되었다!"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('shd_atk', '초록불', '지정한 적을 공격합니다.', "assets/fight/card1.jpg", attack, Need.Enemy),
        Skill('shd_cc', '정지', '빨간불이 되어 상대가 다음 신호를 기다립니다.', "assets/player/no_img.png", attack, Need.Enemy), #지정한 한명 스턴넣기
        Skill('shd_def', '빨간불', '정지하여 자신을 보호합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]

