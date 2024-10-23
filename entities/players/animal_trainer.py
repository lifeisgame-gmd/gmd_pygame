from typing import Any
import random

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class Animal_Trainer(Player):

    def __init__(self):
        super().__init__('동물조련사',"assets/player/cat.png", 10, 4)
        self.animal = ""


    def call_animal(self, fight_data, additional_data):
        R = random(1,100)
        if R <= 70:
          self.animal = "개"
        else if R <= 95:
          self.animal = "호랑이"
        else:
          self.animal = "용"
        return "동물 조련사는 " +self.animal + "을(를) 불러냈다!"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('cat_atk', '냥냥 펀치', '지정한 적을 공격합니다.', "assets/player/loli.jpg", call_animal, Need.Enemy),
        Skill('cat_def', '냥냥 방어', '털로 몸을 감싸 방어합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]

