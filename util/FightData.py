from typing import List


class FightData:
    def __init__(self,ally: List['Player'],  enemy: List['Monster']):
        self.ally = ally
        self.enemy = enemy
