import pygame

class Button:
    def __init__(self, image, width=None, height=None, on_click=None, x=0, y=0):
        # 이미지의 원래 크기를 가져옵니다.
        original_width, original_height = image.get_size()

        # width와 height가 None일 경우 원래 크기를 사용합니다.
        self.width = width if width is not None else original_width
        self.height = height if height is not None else original_height

        # 이미지를 지정된 크기로 변환합니다.
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()

        # 버튼의 중앙을 기준으로 위치 설정
        self.rect.center = (x, y)

        self.on_click = on_click  # 클릭 시 실행할 함수

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)  # rect의 위치를 사용하여 그립니다.

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            if self.on_click:
                self.on_click()  # 클릭 시 함수 실행
