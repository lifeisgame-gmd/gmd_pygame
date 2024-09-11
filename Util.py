import pygame
from pygame.examples.cursors import image

from Button import Button


def collide(x, y, width, height):
    pos = pygame.mouse.get_pos()
    if (x < pos[0]) and (pos[0] < + x+width) and (y < pos[1]) and (pos[1] < + y+height):
        return True
    else:
        return False



class Image:
    def __init__(self, src):
        self.image = pygame.image.load(src)

    def scale(self, width, height):
        temp_image = self
        temp_image.image = pygame.transform.scale(temp_image.image, (width, height))
        return temp_image

    def subsurface(self, x, y, width, height):
        temp_image = self
        temp_image.image = image.subsurface((x, y, width,height ))
        return temp_image

    def button(self, x, y, on_click):
        return Button(self.image, x=x, y=y, on_click=on_click)

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))