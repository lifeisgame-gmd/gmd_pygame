import copy

from entities.monsters.slime import Slime
from entities.players.cat import Cat
from managers.Entities import Player, Monster


class MonsterManager:
    arr: dict[str, Monster] = {}
    @staticmethod
    def init():
        MonsterManager.arr['slime'] = Slime("슬라임", "assets/monster/slime.png", 10, 1)

    @staticmethod
    def get(name: str, lvl: int) -> Monster:
        copied = copy.deepcopy(MonsterManager.arr[name]).lvl_up(lvl-1)
        copied.load_image()
        return copied

class PlayerManager:
    arr: dict[str, Player] = {}

    @staticmethod
    def init():
        PlayerManager.arr['cat'] = Cat('cat',"assets/player/cat.png", 10, 1, 1)

    @staticmethod
    def get(name: str, lvl: int) -> Player:
        copied = copy.deepcopy(PlayerManager.arr[name]).lvl_up(lvl-1)
        copied.load_image()
        return copied