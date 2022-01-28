from .settings import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        self._layer = WALL_LAYER
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x*TILE_SIZE
        self.rect.y = y*TILE_SIZE
