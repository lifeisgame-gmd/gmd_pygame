import copy

from entities.monsters.Slime import Slime
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

    @staticmethod
    def get(name: str, lvl: int) -> Monster:
        copied = copy.deepcopy(MonsterManager.arr[name]).lvl_up(lvl-1)
        copied.load_image()
        return copied

class PlayerManager:
    arr: dict[str, Player] = {}

    @staticmethod
    def init():
        PlayerManager.arr['AnimalTrainer'] = AnimalTrainer()
        PlayerManager.arr['Archer'] = Archer()
        PlayerManager.arr['Batman'] = Batman()
        PlayerManager.arr['Bomber'] = Bomber()
        PlayerManager.arr['Cat'] = Cat()
        PlayerManager.arr['CloseCombatant'] = CloseCombatant()
        PlayerManager.arr['Dog'] = Dog()
        PlayerManager.arr['Fanatic'] = Fanatic()
        PlayerManager.arr['HolyKnight'] = HolyKnight()
        PlayerManager.arr['Knight'] = Knight()
        PlayerManager.arr['LightningRat'] = LightningRat()
        PlayerManager.arr['MatNanInSungBa'] = MatNanInSungBa()
        PlayerManager.arr['MyakMyak'] = MyakMyak()
        PlayerManager.arr['NewPlayer'] = NewPlayer()
        PlayerManager.arr['OmnivorePlant'] = OmnivorePlant()
        PlayerManager.arr['Potioner'] = Potioner()
        PlayerManager.arr['Priest'] = Priest()
        PlayerManager.arr['Samurai'] = Samurai()
        PlayerManager.arr['Stone'] = Stone()
        PlayerManager.arr['TrafficLight'] = TrafficLight()
        PlayerManager.arr['Wizard'] = Wizard()

    @staticmethod
    def get(name: str, lvl: int) -> Player:
        copied = copy.deepcopy(PlayerManager.arr[name]).lvl_up(lvl-1)
        copied.load_image()
        return copied