import os
from pprint import pprint

import pygame
import json

from pygame.examples.cursors import image

from managers.Entities import Monster
from managers.EntityManager import MonsterManager
from managers.MapManager import MapManager
from util.FightData import FightData
from util.PlayerData import PlayerData
from util.Util import Image
from typing import List, Optional

"""
Example Scene
"""

# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager):
    global manager
    global fight_background
    global fight_skill_card
    global fight_skill_card2
    global enemy_arr
    global ally_arr
    global fight_data


    manager = scene_manager
    fight_background = Image("assets/fight/fight_bg.jpg").scale(1920, 1080)
    fight_skill_card=pygame.image.load("assets/fight/card1.jpg")
    fight_skill_card2=pygame.image.load("assets/fight/card2.jpg")

    json_data = MapManager.map_data
    map_data = json_data['stage'][MapManager.cur]

    enemies: List[Optional[Monster]] = [MonsterManager.get(i['id'], i['lvl']) for i in map_data['enemies']]
    for i in range(4-len(enemies)):
        enemies.append(None)

    fight_data = FightData(PlayerData.party, enemies)
    print(fight_data)

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    fight_background.draw(screen, 0, 0)
    screen.blit(fight_skill_card, (960,780))
    screen.blit(fight_skill_card2, (830,780))
    for i in range(len(fight_data.ally)):
        if fight_data.ally[i] is not None:
            fight_data.ally[i].image.scale(128, 128).flip(True, False).draw(screen, i*128+64, 540, is_center=True)


# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
