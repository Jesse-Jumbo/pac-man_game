import pygame.draw

from .settings import *

class Dot(pygame.sprite.Sprite):
    def __init__(self, game):
        self._layer = DOT_LAYER
        self.groups = game.all_sprites, game.dots
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.angle = 0
        self.image = game.small_dot_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-self.rect.width)
        self.rect.y = random.randint(0, HEIGHT-self.rect.height)

    # def update(self) -> None:
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

