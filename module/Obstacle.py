import pygame.math

from .settings import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, sprite_group, x, y, width, height, object_id=0):
        self.groups = sprite_group
        super().__init__(self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, width, height)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.node_value = object_id
        self.node_pos = pygame.math.Vector2(x, y)