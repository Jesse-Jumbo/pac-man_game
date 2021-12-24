from .setting import *
from .Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y)

    def update(self, *args, **kwargs) -> None:
        self.blue_module()
