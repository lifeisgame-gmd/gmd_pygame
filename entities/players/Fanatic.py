from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class Priest(Player):

    def __init__(self):
        super().__init__('성직자',"assets/player/Priest.png", 2, 3, 1) #공,체,1
        


    def buff(self, fight_data, additional_data):
        buff_time = fight_data.turn + 3
        self.att += 3 # 공격력은 atk입니다.

        return "성직자의 방어력이 3 증가했다!" # 방어력이 증가한 적은 없습니다.

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"
    
    def heal(self, fight_data: FightData, additional_data: Entity):
        additional_data.hp_c = min(additional_data.hp_c + self.atk + 5, additional_data.hp_m)
        return additional_data.name + "을(를) " + str(self.atk)+"만큼 회복시켰다!"

    skills = [
        Skill('Prist_Atk', '신을 맞이하라', '지정한 적에게 25% 확률로 강력한 공격을 합니다.', "assets/fight/card1.jpg", attack, Need.Enemy),
        Skill('Prist_Def', '그날이 오고있다', '일정 턴 동안 자신의 공격력 강화', "assets/player/no_img.png", buff, Need.Self), 
        Skill('Prist_Heal', '신의 축복일지니!', '자신의 hp를 회복시킨다.', "assets/player/no_img.png", heal, Need.Self)
    ]

    def turn(self, fight_data):
        pass
    