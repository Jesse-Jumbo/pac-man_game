from .setting import *
from .Ghost import Ghost


class PinkGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.pink_ghost_d
        self.origin_img = game.pink_ghost_d
        self.up_img = game.pink_ghost_u
        self.right_img = game.pink_ghost_r
        self.left_image = game.pink_ghost_l

    def update(self, *args, **kwargs) -> None:
        if 1 < self.count_time <= 20:
            self.move(WIDTH-180, 30)
        elif self.count_time <= 40:
            self.scatter_model(WIDTH-180, 30)
        elif self.count_time == 60:
            self.origin_img = self.game.pink_ghost_d
            self.up_img = self.game.pink_ghost_u
            self.right_img = self.game.pink_ghost_r
            self.left_image = self.game.pink_ghost_l
            self.count_time = 0
        else:
            self.blue_module()
        self.count_time += 0.015625
