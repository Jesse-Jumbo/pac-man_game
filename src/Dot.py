from .env import *


class Dot(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        self._layer = DOT_LAYER
        super().__init__()
        self.rect = pygame.Rect(x, y, all_object_size[0], all_object_size[1])
        self.hit_rect = pygame.Rect(x, y, object_hit_size[0], object_hit_size[1])
        self.hit_rect.center = self.rect.center

    def update(self) -> None:
        pass

    def get_position(self):
        return self.rect.left, self.rect.top
