import pygame.draw

from .settings import *


class Dot(pygame.sprite.Sprite):
    def __init__(self, img,  x, y):
        self._layer = DOT_LAYER
        super().__init__()
        self.angle = 0
        self.image = img
        self.rect = self.image.get_rect()
        self.hit_rect = DOT_HIT_RECT.copy()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect.center = self.rect.center

    def update(self) -> None:
        pass
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

