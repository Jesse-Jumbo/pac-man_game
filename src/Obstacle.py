import pygame.math

from .env import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, img,  x: float, y: float):
        super().__init__()
        self.image = img
        self.rect = ALL_OBJECT_SIZE.copy()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.pos = pygame.math.Vector2(x, y)
        # TODO unified node grid pos
        self.node_pos = pygame.math.Vector2(x / TILE_X_SIZE, y / TILE_Y_SIZE)

    def get_position(self, xy: str):
        if xy == "x":
            return self.rect.x
        elif xy == "y":
            return self.rect.y
        else:
            return "please input x or y to get position"
