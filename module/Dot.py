import pygame.draw

from .collide_with_walls import collide_with_walls
from .settings import *

class Dot(pygame.sprite.Sprite):
    def __init__(self, game):
        self._layer = DOT_LAYER
        self.groups = game.all_sprites, game.dots
        super().__init__(self.groups)
        self.game = game
        self.angle = 0
        self.image = game.small_dot_img
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.rect.x = random.randint(0, WIDTH - TILE_SIZE)
        self.rect.y = random.randint(0, HEIGHT - TILE_SIZE)

    def update(self) -> None:
        collide_with_walls(self, self.game.walls, "wall")
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

