from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class Priest(Player):

    def __init__(self):
        super().__init__('성직자',"assets/player/Priest.png", 2, 3, 1) #공,체,1
        
    def turn():
        print('Hello, World!')

    def defend(self, fight_data, additional_data):
        self.protect += 3
        return "성직자의 방어력이 3 증가했다!"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"
    
    def heal(self, fight_data: FightData, additional_data: Entity):
        additional_data.hp_c = min(additional_data.hp_c + self.atk + 5, additional_data.hp_m)
        return additional_data.name + "을(를) " + min(additional_data.hp_c + self.atk + 5, additional_data.hp_m)+"만큼 회복시켰다!"

    skills = [
        Skill('Prist_Atk', '신성한 힘', '지정한 적을 신성한 힘으로 공격합니다.', "assets/fight/card1.jpg", attack, Need.Enemy),
        Skill('Prist_Def', '신의 가호', '신의 가호가 몸을 지켜줍니다.', "assets/player/no_img.png", defend, Need.Self), 
        Skill('Prist_Heal', '성스러운 물', '아군 1명에게 성수를 내려 피를 회복시킵니다.', "assets/player/no_img.png", heal, Need.Ally)
    ]
