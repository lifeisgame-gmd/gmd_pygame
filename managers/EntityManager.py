import copy

from entities.monsters.Slime import Slime
from entities.players.NewPlayer import NewPlayer
from entities.players.Cat import Cat
from managers.Entities import Player, Monster


class MonsterManager:
    arr: dict[str, Monster] = {}
    @staticmethod
    def init():
        MonsterManager.arr['slime'] = Slime()

    @staticmethod
    def get(name: str, lvl: int) -> Monster:
        copied = copy.deepcopy(MonsterManager.arr[name]).lvl_up(lvl-1)
        copied.load_image()
        return copied

class PlayerManager:
    arr: dict[str, Player] = {}

    @staticmethod
    def init():
        PlayerManager.arr['cat'] = Cat()
        PlayerManager.arr['newPlayer'] = NewPlayer()

    @staticmethod
    def get(name: str, lvl: int) -> Player:
        copied = copy.deepcopy(PlayerManager.arr[name]).lvl_up(lvl-1)
        copied.load_image()
        return copied