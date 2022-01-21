from .collide_hit_rect import collide_hit_rect
from .settings import *


class Point(pygame.sprite.Sprite):
    def __init__(self, game, img, x, y):
        self._layer = POINT_LAYER
        self.groups = game.all_sprites, game.points
        super().__init__(self.groups)
        self.game = game
        self.image = img
        self.rect = self.image.get_rect()
        self.hit_rect = POINT_HIT_RECT.copy()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect.center = self.rect.center

    def update(self, *args, **kwargs) -> None:
        pass
