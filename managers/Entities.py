from abc import abstractmethod

from source.conf import project
from util.Util import Image


class Entity:

    def __init__(self, name: str, src: str, hp: int, atk: int, lvl=1):
        """

        :rtype: object
        """
        self.atk = 0
        self.name = name
        self.src = src
        self.hp_o = hp # original. 레벨업 당 계수
        self.hp_c = hp # current. 현재 체력
        self.hp_m = hp # max. 최대 체력
        self.atk_o = atk
        self.protect = 0
        self.lvl = lvl
        self.tag = []

    def damage(self, atk):
        self.hp_c -= max(atk - self.protect, 0)

    def lvl_up(self, lvl: int):
        self.lvl += lvl
        self.hp_c += self.hp_o * self.lvl - self.hp_m
        self.hp_m = self.hp_o * self.lvl
        self.atk = self.atk_o * self.lvl
        return self

    def load_image(self):
        self.image = Image(self.src)

    def turn(self, fight_data):
        return ""

    def initialize(self):
        self.tag = []


class Monster(Entity):

    def __init__(self, name: str, src: str, hp: int, atk: int, lvl=1):
        super().__init__(name, src, hp, atk, lvl)

    @abstractmethod
    def action(self, fight_data):
        pass


class Player(Entity):
    skills = []
    def load_image(self):
        super().load_image()
        for i in range(len(self.skills)):
            self.skills[i].image = Image(self.skills[i].src)
    pass
