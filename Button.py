import pygame

class Button:
    def __init__(self, image, width=None, height=None, on_click=None, x=0, y=0):
        original_width, original_height = image.get_size()
        self.width = width if width is not None else original_width
        self.height = height if height is not None else original_height
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.on_click = on_click

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            if self.on_click:
                self.on_click()

# asdf
