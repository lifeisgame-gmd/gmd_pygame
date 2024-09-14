import copy

from entities.monsters.slime import Slime
from managers.Entities import Player
from util.FightData import FightData
from util.Skill import Skill


def init():
    MonsterManager.arr['slime'] = Slime("슬라임", "assets/monster/slime.png", 10, 1)


def get(name: str, lvl: int):
    return copy.deepcopy(MonsterManager.arr[name]).lvl_up(lvl)

class MonsterManager:
    arr = {}

class PlayerManager:
    arr = {}

    def __init__(self):
        def skill(fight_data: FightData, subject: Player):
            fight_data.enemy[0].damage(subject.atk)
        PlayerManager.arr['cat'] = Player("cat", "../assets/player/cat.png", 10, 1, [Skill(skill)])