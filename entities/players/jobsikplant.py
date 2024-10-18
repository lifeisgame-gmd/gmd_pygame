from managers.Entities import Monster
from util.FightData import FightData


class jobsikplant(Player):

    def __init__(self):
        super().__init__('잡식식물',"assets/player/cat.png", 10, 4, 1)


    def defend(self, fight_data, additional_data: Entity):
        additional_data.hp_c = min(additional_data.hp_c + 10, additional_data.hp_m)
        return "잡식식물이 햇빛을 받고 회복했다!"

    def attack(self, fight_data: FightData, additional_data: Entity):
        additional_data.damage(self.atk)
        return additional_data.name + "을(를) " + str(self.atk)+"의 데미지로 공격했다!"

    skills = [
        Skill('jobsikplant_atk', '깨물기', '지정한 적을 깨물어서 공격합니다.', "assets/fight/card1.jpg", attack, Need.Enemy),
        Skill('jobsikplant_def', '광합성 치유', '햇빛을 받고 잡식식물이 회복합니다.', "assets/player/no_img.png", defend, Need.Self)
    ]

