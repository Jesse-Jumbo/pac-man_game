from .setting import *
from .Ghost import Ghost

class RedGhost(Ghost):
    def __init__(self, color, centerx, centery):
        super().__init__(color, centerx, centery)
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self, *args, **kwargs) -> None:
        Ghost().blue_module()
