from pygame.locals import *
import pygame

def collide(x, y, width, height):
    pos = pygame.mouse.get_pos()
    if (x < pos[0]) and (pos[0] < + x+width) and (y < pos[1]) and (pos[1] < + y+height):
        return True
    else:
        return False
