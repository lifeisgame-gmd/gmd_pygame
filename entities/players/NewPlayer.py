from managers.Entities import Player
from util.Skill import Skill, Need


class NewPlayer(Player):
    def __init__(self):
        super().__init__('별', "assets/player/NewPlayer.png", 10, 2)

    def skill1(self, fight_data, additional_data):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"


    skills = [
        Skill('newPlayer_atk', '공격', '지정한 적을 공격합니다', "assets/player/no_img.png", skill1, Need.Enemy)
    ]
