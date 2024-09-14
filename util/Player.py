from typing import List
from Skill import Skill


class Player:
    def __init__(self, name: str, src: str, hp: int, atk: int, need: int, skills: List[Skill], lvl=1):
        self.name = name
        self.src = src
        self.hp = hp
        self.atk = atk
        self.skills = skills
        self.lvl = lvl
        self.need = need

    def damage(self, damage):
        self.hp -= damage