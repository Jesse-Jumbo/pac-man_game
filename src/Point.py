from .env import *


class Point(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        self._layer = POINT_LAYER
        super().__init__()
        self.rect = ALL_OBJECT_SIZE.copy()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect = POINT_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center

    def update(self, *args, **kwargs) -> None:
        pass

    def get_position(self, xy: str):
        if xy == "x":
            return self.rect.x
        elif xy == "y":
            return self.rect.y
        else:
            return "please input x or y to get position"
