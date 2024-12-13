import copy
import pygame
from util.Button import Button


def collide(x, y, width, height):
    pos = pygame.mouse.get_pos()
    return (x < pos[0] < x + width) and (y < pos[1] < y + height)


class Image:
    def __init__(self, src):
        self.image = pygame.image.load(src)

    def scale(self, width, height):
        temp_image = self
        temp_image.image = pygame.transform.scale(temp_image.image, (width, height))
        return temp_image

    def subsurface(self, x, y, width, height):
        temp_image = copy.copy(self)
        temp_image.image = temp_image.image.subsurface((x, y, width, height))
        return temp_image

    def flip(self, x: bool, y: bool):
        temp_image = copy.copy(self)
        temp_image.image = pygame.transform.flip(temp_image.image, x, y)
        return temp_image

    def button(self, x, y, on_click, is_center=False) -> Button:
        return Button(self.image, x=x, y=y, on_click=on_click, is_center=is_center)

    def draw(self, screen, x, y, is_center =False):
        if is_center:
            screen.blit(self.image, (x-self.image.get_size()[0]/2, y-self.image.get_size()[1]/2))
        else:
            screen.blit(self.image, (x, y))

    def to_tile_set_by_size(self, width, height):
        tile_width = width
        tile_height = height
        image_width, image_height = self.image.get_size()

        cols = image_width // tile_width
        rows = image_height // tile_height

        tile_set = []

        for row in range(rows):
            row_tiles = []
            for col in range(cols):
                x = col * tile_width
                y = row * tile_height
                tile = self.subsurface(x, y, tile_width-1, tile_height-1)
                row_tiles.append(tile)
            tile_set.append(row_tiles)

        return tile_set

    def to_tile_set_by_count(self, x_amount, y_amount):
        image_width, image_height = self.image.get_size()

        tile_width = image_width // x_amount
        tile_height = image_height // y_amount
        return self.to_tile_set_by_size(tile_width, tile_height)