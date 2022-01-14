import pygame.math

from .settings import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, sprite_group, img,  x=0, y=0, width=0, height=0, object_id=0):
        self.groups = sprite_group, game.all_sprites
        super().__init__(self.groups)
        self.game = game
        self.image = img
        self.rect = self.image.get_rect()
        # self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        # self.node_value = object_id
        self.node_pos = pygame.math.Vector2(x, y)
