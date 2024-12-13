import copy

from entities.monsters.DarkPriest import DarkPriest
from entities.monsters.Dragon import Dragon
from entities.monsters.SkeletonArcher import SkeletonArcher
from entities.monsters.Slime import Slime
from entities.monsters.livingarmor import LivingArmor
from entities.players.AnimalTrainer import AnimalTrainer
from entities.players.Archer import Archer
from entities.players.Batman import Batman
from entities.players.Bomber import Bomber
from entities.players.Cat import Cat
from entities.players.CloseCombatant import CloseCombatant
from entities.players.Dog import Dog
from entities.players.Fanatic import Fanatic
from entities.players.HolyKnight import HolyKnight
from entities.players.Knight import Knight
from entities.players.LightningRat import LightningRat
from entities.players.MatNanInSungBa import MatNanInSungBa
from entities.players.MyakMyak import MyakMyak
from entities.players.NewPlayer import NewPlayer
from entities.players.OmnivorePlant import OmnivorePlant
from entities.players.Potioner import Potioner
from entities.players.Priest import Priest
from entities.players.Samurai import Samurai
from entities.players.Stone import Stone
from entities.players.TrafficLight import TrafficLight
from entities.players.Wizard import Wizard
from managers.Entities import Player, Monster


class MonsterManager:
    arr: dict[str, Monster] = {}
    @staticmethod
    def init():
        MonsterManager.arr['slime'] = Slime()
        MonsterManager.arr['dragon'] = Dragon()
        MonsterManager.arr['dark_priest'] = DarkPriest()
        MonsterManager.arr['skeleton_archer'] = SkeletonArcher()
        MonsterManager.arr['livingarmor'] = LivingArmor()

    @staticmethod
    def get(name: str, lvl: int) -> Monster:
        copied = copy.deepcopy(MonsterManager.arr[name]).lvl_up(lvl-1)
        copied.load_image()
        return copied

class PlayerManager:
    arr: dict[str, Player] = {}

    @staticmethod
    def init():
        PlayerManager.arr[AnimalTrainer().name] = AnimalTrainer()
        PlayerManager.arr[Archer().name] = Archer()
        PlayerManager.arr[Batman().name] = Batman()
        PlayerManager.arr[Bomber().name] = Bomber()
        PlayerManager.arr[Cat().name] = Cat()
        PlayerManager.arr[CloseCombatant().name] = CloseCombatant()
        PlayerManager.arr[Dog().name] = Dog()
        PlayerManager.arr[Fanatic().name] = Fanatic()
        PlayerManager.arr[HolyKnight().name] = HolyKnight()
        PlayerManager.arr[Knight().name] = Knight()
        PlayerManager.arr[LightningRat().name] = LightningRat()
        PlayerManager.arr[MatNanInSungBa().name] = MatNanInSungBa()
        PlayerManager.arr[MyakMyak().name] = MyakMyak()
        PlayerManager.arr[NewPlayer().name] = NewPlayer()
        PlayerManager.arr[OmnivorePlant().name] = OmnivorePlant()
        PlayerManager.arr[Potioner().name] = Potioner()
        PlayerManager.arr[Priest().name] = Priest()
        PlayerManager.arr[Samurai().name] = Samurai()
        PlayerManager.arr[Stone().name] = Stone()
        PlayerManager.arr[TrafficLight().name] = TrafficLight()
        PlayerManager.arr[Wizard().name] = Wizard()


    @staticmethod
    def get(name: str, lvl: int) -> Player:
        copied = copy.deepcopy(PlayerManager.arr[name]).lvl_up(lvl-1)
        copied.load_image()
        return copied