from typing import Any
import random

from managers.Entities import Player, Entity
from util.FightData import FightData
from util.Skill import Skill, Need

global target
target = [0,0,0,0]

class Animal_Trainer(Player):

    def __init__(self):
        super().__init__('동물조련사',"assets/player/cat.png", 2, 4)
        self.animal = ""
        self.enemy_buff_time = [0,0,0,0]


    def call_animal(self, fight_data, additional_data):
        R = random(1,100)
        if R <= 70:
          self.animal = "개"
          if len(self.skills)==2:
            del self.skills [1]
          else:
            del self.skills[1]
            del self.skills[2]          
          self.skills.append(Skill('bite','물어!','지정한 상대 1명을 공격한다.',"assets/player/no_img",bite, Need.Enemy))
          self.skills.append(Skill('scar_licking','상처핥기','스스로의 hp를 약간 회복한다.',"assets/player/no_img",licking, Need.self))
        elif R <= 95:
          self.animal = "호랑이"
          if len(self.skills)==2:
            del self.skills [1]
          else:
            del self.skills[1]
            del self.skills[2]
          self.skills.append(Skill('growling','울음소리','지정한 상대 1명의 공격력을 낮춘다.',"assets/player/no_img",growling, Need.Enemy))
        else:
          self.animal = "용"
          if len(self.skills)==2:
            del self.skills [1]
          else:
            del self.skills[1]
            del self.skills[2]    
        return "동물 조련사는 " +self.animal + "을(를) 불러냈다!"
        
    def licking(self, fight_data: FightData, additional_data):
      R = random(1,3)
      if R == 1:
        if self.atk * (45/100)<1:
          self.hp_c += 1
        else:
          self.hp_c += self.atk * (45/100)
      elif R == 2:
        if self.atk * (50/100)<1:
          self.hp_c += 1
        else:
          self.hp_c += self.atk * (60/100)
      elif R == 3:
        if self.atk * (60/100)<1:
          self.hp_c += 1
        else:
          self.hp_c += self.atk * (45/100)
      if self.hp_c > self.hp_m:
        self.hp_c = self.hp_m
      
    def bite(self, fight_data: FightData, additional_data: Entity):
      R = random(1,3)
      if R == 1:
        additional_data.damage(self.atk*1.5)
      elif R == 2:
        additional_data.damage(self.atk*1.7)
      else:
        additional_data.damage(self.atk*2)
      
    def growling(self, fight_data:FightData, additional_data: Entity):
      for i in range(0,4):
        if target[i] == 0:
          target[i] = additional_data
          self.enemy_buff_time[i] = fight_data + 3
      self.original_enemy_atk = additional_data.atk
      additional_data.atk(additional_data.atk * (8/10) )
      return additional_data.name + "의 공격력을 " + additional_data.atk * (8/10) + "만큼 감소시켰다!"
    
    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('call_animal', '동물 부르기', '랜덤으로 동물을 부릅니다.', "assets/player/loli.jpg", call_animal, Need.Enemy),
        Skill('whip', '채찍질하기', '동물조련사가 상대방을 공격합니다.', "assets/player/no_img.png", attack, Need.Enemy)
    ]
    
    def turn(self, fight_data):
        global target
        for i in range(0,4):
          if self.enemy_buff_time[i] == fight_data.turn and target[i] != 0:
            target[i].atk = target[i].atk_o
            self.enemy_buff_time = 0
        pass