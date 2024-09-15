import pygame

from SceneManager import SceneManager
from managers.EntityManager import PlayerManager, MonsterManager
from managers.MapManager import MapManager
from util.PlayerData import PlayerData


# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager: SceneManager):
    global manager
    manager= scene_manager

    PlayerManager.init()
    MonsterManager.init()
    MapManager.init()

    PlayerData.debug_init()

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    manager.change_scene('start')
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    pass

# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
