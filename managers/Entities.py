from abc import abstractmethod
from source.conf import project
from util.Util import Image


class Entity:

    def __init__(self, name: str, src: str, hp: int, atk: int, lvl=1):
        """

        :rtype: object
        """
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
        self.lvl += lvl
        self.hp = self.hp_o * self.lvl
        self.atk = self.atk_o * self.lvl
        return self

    def load_image(self):
        self.image = Image(self.src)


class Monster(Entity):

    def __init__(self, name: str, src: str, hp: int, atk: int, lvl=1):
        super().__init__(name, src, hp, atk, lvl)

    @abstractmethod
    def action(self, fight_data):
        pass


class Player(Entity):
    skills = []
    pass
