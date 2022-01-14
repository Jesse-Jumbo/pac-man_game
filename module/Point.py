from .settings import *


class Point(pygame.sprite.Sprite):
    def __init__(self, game, img, x, y):
        self._layer = POINT_LAYER
        self.groups = game.all_sprites, game.points
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
