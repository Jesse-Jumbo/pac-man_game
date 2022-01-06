from .settings import *


class Point(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = POINT_LAYER
        self.groups = game.all_sprites, game.points
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = game.big_dot_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y