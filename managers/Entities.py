from abc import abstractmethod
from source.conf import project
from util.FightData import FightData


class Entity:

    def __init__(self, name: str, src: str, hp: int, atk: int, lvl=1):
        self.atk = 0
        self.hp = 0
        self.name = name
        self.src = src
        self.hp_o = hp
        self.atk_o = atk
        self.protect = 0
        self.lvl = lvl

    def damage(self, atk):
        self.hp = self.hp_o - max(atk - project, 0)

    def lvl_up(self, lvl: int):
        self.hp = self.hp_o * lvl
        self.atk = self.atk_o * lvl
        return self


class Monster(Entity):

    def __init__(self, name: str, src: str, hp: int, atk: int, lvl=1):
        super().__init__(name, src, hp, atk, lvl)

    @abstractmethod
    def action(self, fight_data: FightData):
        pass


class Player(Entity):
    pass
