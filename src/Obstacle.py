import pygame.math

from games.pac_man.module.settings import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, img,  x: float=0, y: float=0, width: float=0, height: float=0):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.pos = pygame.math.Vector2(x, y)
        self.node_pos = pygame.math.Vector2(x / TILE_SIZE, y / TILE_SIZE)
