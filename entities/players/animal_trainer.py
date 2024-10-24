from typing import Any
import random

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need


class Animal_Trainer(Player):

    def __init__(self):
        super().__init__('동물조련사',"assets/player/cat.png", 2, 4)
        self.animal = ""


    def call_animal(self, fight_data, additional_data):
        R = random(1,100)
        if R <= 70:
          self.animal = "개"
          del self.skills [1]
          self.skills.append(Skill('bite','물어!','지정한 상대 1명을 공격한다.',"assets/player/no_img",bite, Need.Enemy))
          self.skills.append(Skill('scar_licking','상처핥기','스스로의 hp를 약간 회복한다.',"assets/player/no_img",licking, Need.self))
        else if R <= 95:
          self.animal = "호랑이"
        else:
          self.animal = "용"
        return "동물 조련사는 " +self.animal + "을(를) 불러냈다!"
        
    def licking(self, fight_data: FightData, additional_data):
      R = random(1,3)
      if R == 1
        if self.atk * (45/100)<1:
          self.hp_c += 1
        else:
          self.hp_c += self.atk * (45/100)
      else if R == 2
        if self.atk * (50/100)<1:
          self.hp_c += 1
        else:
          self.hp_c += self.atk * (60/100)
      else if R == 1
        if self.atk * (60/100)<1:
          self.hp_c += 1
        else:
          self.hp_c += self.atk * (45/100)
      if self.hp_c > self.hp_m:
        self.hp_c = self.hp_m
      
    def bite(self, fight_data: FightData, additional_data: Entity):
    
    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('call_animal', '동물 부르기', '랜덤으로 동물을 부릅니다.', "assets/player/loli.jpg", call_animal, Need.Enemy),
        Skill('whip', '채찍질하기', '동물조련사가 상대방을 공격합니다.', "assets/player/no_img.png", attack, Need.Enemy)
    ]
    
    def turn(self, fight_data,buff_time,original_atk):
        if self.buff_time == fight_data.turn:
            self.atk = self.original_atk
            self.buff_time = None
        pass
    

