from typing import Any

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class MatNanInSungBa(Player):

    def __init__(self):
        super().__init__('맛난인성봐',"assets/player/mat.png", 1000, 1000, 1000)

    def stun_sk(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        for i in range(len(fight_data.enemy)):
            if fight_data.enemy[i] is not additional_data:
                continue
            if i > 1 and fight_data.enemy[i-1] is not None:
                fight_data.enemy[i-1].damage(self.atk)
            fight_data.enemy[i].damage(self.atk)
            if i < 4 and fight_data.enemy[i+1] is not None:
                fight_data.enemy[i+1].damage(self.atk) #스턴 3턴동안 넣기


    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
            Skill('matnaninsungba_atk1', '멈춰!', '모든 적을 기절시킵니다', "assets/player/loli.jpg", attack, Need.Enemy),
        Skill('Matnaninsungba_atk2', '냥냥 방어', '폭탄들 던져 1명에게 공격력 만큼의 데미지를 준다.', "assets/player/no_img.png", stun_sk, Need.Enemy)
    ]

