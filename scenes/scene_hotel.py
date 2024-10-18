import pygame
from util.Button import Button

"""
Example Scene
"""

# setup 메소드는 씬이 불러와질 때마다 실행되는 메소드입니다.
def setup(scene_manager):
    global manager
    global background
    global hotel_master
    global hotel_master_chatbox
    global sleep_button #hp회복
    global back_button #마을로 돌아감.
    global game_font #글로벌로 폰트 생성.
    global greeting_text
    global back_button_text
    manager = scene_manager

    background = pygame.image.load("assets/hotel_background.png") #배경
    background = pygame.transform.scale(background, (1920, 1080))
    hotel_master_image = pygame.image.load("assets/hotel_master.png")#호텔 주인 이미지
    hotel_master = pygame.transform.scale(hotel_master_image, (500, 700)) 
    hotel_master_chatbox_image = pygame.image.load("assets/hotel_master_chatbox.png")#호텔 주인 챗박스 이미지
    hotel_master_chatbox = pygame.transform.scale(hotel_master_chatbox_image, (1920, 400))
    Button_image = pygame.image.load("assets/hotel_master_chatbox.png")
    Button_image = pygame.transform.scale(hotel_master_chatbox_image, (300, 100))
    back_button = Button(Button_image, on_click=lambda: manager.change_scene('town'), x=150, y=650)

    game_font = pygame.font.Font(r"assets\font\neodgm_code\neodgm_code.ttf", 30) #(r<<<<필수임진짜로없으면경로안불러와지니제발넣어줘"경로/글꼴", 크기) #텍스트에 쓸 글꼴 설정
    
    #텍스트
    greeting_text = game_font.render("미천한 필멸자가 또 다시 영원의 땅에 발을 들이는구나.", True,(0,0,0)) #("텍스트",안티에일어싱 여부,(R,G,B) 또는 색깔 대문자로 써 넣기.)
    back_button_text = game_font.render("뭐야 이건?", True,(0,0,0))

# 씬이 불러와진 상태일 때, 이벤트가 작동할 시 실행되는 메소드입니다.
def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        back_button.check_click(event.pos)
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 실행되는 메소드입니다.
def update():
    pass

# 씬이 불러와진 상태일 때, 각 프레임마다 update 메소드 뒤에 실행되는 메소드입니다.
def draw(screen):
    screen.blit(background, (0, 0))
    screen.blit(hotel_master, (1400, 200))
    screen.blit(hotel_master_chatbox, (0, 700))
    
    back_button.draw(screen)
    #출력
    screen.blit(greeting_text,(20,730))
    screen.blit(back_button_text,(20,630))
    pass

# 다른 씬으로 넘어갈 때 실행되는 메소드입니다.
def cleanup():
    pass
