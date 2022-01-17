import pygame.draw

from .collide_sprite_with_walls import collide_with_walls
from .settings import *

class Dot(pygame.sprite.Sprite):
    def __init__(self, game, img,  x, y):
        self._layer = DOT_LAYER
        self.groups = game.all_sprites, game.dots
        super().__init__(self.groups)
        self.game = game
        self.angle = 0
        self.image = img
        self.rect = self.image.get_rect()
        self.hit_rect = DOT_HIT_RECT
        self.rect.x = x
        self.rect.y = y
        self.hit_rect.center = self.rect.center

    def update(self) -> None:
        pass
        # collide_with_walls(self, self.game.walls, "wall")
    #     self.angle = (self.angle + 10) % 360

    @property
    def dot_data(self):
        return {
            "type": "rect",
            "name": "dot",
            "x": self.rect.x,
            "y": self.rect.y,
            "angle": 0,
            "width": self.rect.width,
            "height": self.rect.height,
        }

