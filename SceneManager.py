import importlib
import pygame

class SceneManager:

    # __init__은 SceneManager 객체가 생성될 때 실행되는 코드입니다. SceneManager 객체는 main.py에서 생성되고 다시 생성될 일은 없습니다.
    def __init__(self, screen):
        self.current_scene = 'start' # 시작 scene을 'start'로 정했으니, scene_start를 실행하겠다는 의미겠네요.
        self.scene_module = None # scene_module은 load_scene에서 불러올 scene 파일입니다. 여기에서는 scene_start.py를 불러와서 저장하겠네요. 아직 없으니 None로 선언만 해줍니다.
        self.screen = screen # Screen은 main.py에서 선언한 screen을 가져옵니다.
        self.change_scene(self.current_scene) # load_scene 메소드에 'start'를 넣어 줬습니다.

    #change_scene 메소드는 신을 바꾸는 메소드입니다.
    def change_scene(self, scene_name): # 입력값은 scene_(이름).py에서 (이름)을 받습니다.
        if self.scene_module: # 이미 불러와진 씬이 있다면?
            self.scene_module.cleanup() # 그 씬에서 정리 메소드를 실행합니다.
        self.current_scene = scene_name # SceneManager의 current_scene 변수에다가 메소드의 입력값을 넣어 주네요.
        self.scene_module = importlib.import_module(f'scene_{scene_name}') # 파일에서 새로운 씬을 불러옵니다.
        self.scene_module.setup(self) # 불러온 씬의 셋업 메소드를 실행합니다.

    def run(self):
        running = True # 게임이 실행 중인지를 정하는 변수입니다.
        clock = pygame.time.Clock() # FPS를 제한하는 데 필요한 시계 클래스입니다.
        fps = 15 # FPS는 임의로 설정했습니다.

        while running: # 실행 중인 동안
            for event in pygame.event.get(): # 이벤트가 작동되었다면
                if event.type == pygame.QUIT: # 이벤트가 종료 이벤트라면
                    running = False # 실행을 중지합니다. 이러면 whlie문이 더 이상 작동하지 않으니 파일 끝으로 가겠죠?
                self.scene_module.handle_event(event) # 이벤트가 작동되었다면, 현재 불러와진 씬 모듈의 handle_event 메소드를 실행합니다.
            self.scene_module.update() # 현재 불러와진 씬 모듈의 update 메소드를 실행합니다.
            self.screen.fill((0, 0, 0)) # draw 메소드를 실행하기 전에, 화면을 검은색으로 채워주네요.
            self.scene_module.draw(self.screen) # 현재 불러와진 씬 모듈의 draw 메소드를 실행합니다. 출력할 screen을 매개변수로 주었네요.
            pygame.display.flip() # draw 메소드를 진행하고 나서, 불러온 그래픽을 반영합니다.
            clock.tick(fps) # 1/fps 시간 동안 기다립니다. 20 fps라면, 0.05초 기다리겠네요.