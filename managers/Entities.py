from abc import abstractmethod
from util.Util import Image


class Entity:
    logger = None

    def __init__(self, name: str, src: str, hp: int, atk: int, lvl=1):
        """

        :rtype: object
        """
        self.stun_time = 0
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
        self.used = False

    def damage(self, atk):
        self.hp_c -= max(atk - self.protect, 0)

    def heal(self, amount):
        self.hp_c += min(self.hp_c+amount, self.hp_m)

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

    def initialize(self, logger):
        self.tag = []
        self.logger = logger

    def stun(self, period: int):
        self.stun_time = period
        self.logger.add(self.name+"이(가) " +str(period)+" 턴까지 기절한다!")


class Monster(Entity):

    def __init__(self, name: str, src: str, hp: int, atk: int, lvl=1):
        super().__init__(name, src, hp, atk)

    @abstractmethod
    def action(self, fight_data):
        pass


class Player(Entity):

    def __init__(self, name: str, src: str, hp: int, atk: int, rank: int, lvl=1):
        self.rank = rank
        super().__init__(name, src, hp, atk, lvl)

    skills = []
    def load_image(self):
        super().load_image()
        for i in range(len(self.skills)):
            self.skills[i].image = Image(self.skills[i].src)
    pass
