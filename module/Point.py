from .collide_hit_rect import collide_hit_rect
from .settings import *


class Point(pygame.sprite.Sprite):
    def __init__(self, img, x: float, y: float):
        self._layer = POINT_LAYER
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.hit_rect = POINT_HIT_RECT.copy()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect.center = self.rect.center

    def update(self, *args, **kwargs) -> None:
        pass
