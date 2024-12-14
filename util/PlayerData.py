from typing import List

from entities.players.Cat import Cat
from managers.Entities import Player
from managers.EntityManager import PlayerManager


class PlayerData:
    player_have: dict[str, Player] = {}
    party: List[Player] = [None for i in range(4)]
    gold: int = 100

    @staticmethod
    def debug_init():
        PlayerData.player_have[Cat().name] = PlayerManager.get(Cat().name, 1)
        PlayerData.party[0] = PlayerManager.get(Cat().name, 1)
        PlayerData.party[1] = PlayerManager.get(Cat().name, 1)
        PlayerData.party[3] = PlayerManager.get(Cat().name, 1)

