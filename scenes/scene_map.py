import math

from managers.MapManager import MapManager
from SceneManager import SceneManager
from util.Util import Image

"""
Example Scene
"""
from_town = False
# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager: SceneManager):
    global indicator, battle_tile, town_tile, background, manager, go_button, back_button
    manager = scene_manager
    
    tile_size = 128

    background = Image("assets/map/map_bg.png").scale(1920, 1080)
    town_tile = Image("assets/map/map_town.png").scale(tile_size, tile_size)
    battle_tile = Image("assets/map/map_battle.png").scale(tile_size, tile_size)
    indicator = Image("assets/map/map_indicator.png").scale(tile_size, tile_size)
    go_button = Image("assets/UI/buttons.png").to_tile_set_by_count(2, 2)[0][0].scale(192, 64).button(960, 700, on_click=None, is_center=True)
    #back_button = Image("assets/UI/back.png").scale(100, 100).button(100, 100, on_click=lambda: managers.change_scene("town"), is_center=True)

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    pass
    #if event.type == pygame.MOUSEBUTTONDOWN:
    #    back_button.check_click(event.pos)

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    background.draw(screen, 0, 0)
    size = town_tile.image.get_size()

    r = math.ceil(1920 / (size[0]))
    cur = 960 - size[0] / 2 - (size[0]-(size[0] / 32)) * (r)
    y = 540 - size[1] / 2

    count = 0
    for i in MapManager.get_map(r):

        if i == "T":
            town_tile.draw(screen, cur, y)
        if i == "E":
            battle_tile.draw(screen, cur, y)
        cur += size[0] - (size[0] / 32)
        count += 1

    indicator.draw(screen, 960 - size[0] / 2, 440)
    go_button.draw(screen)
    #if from_town:
    #    back_button.draw(screen)


# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
