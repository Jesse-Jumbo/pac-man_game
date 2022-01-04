from .setting import *
from .Ghost import Ghost


class OrangeGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.orange_ghost_d
        self.origin_img = game.orange_ghost_d
        self.up_img = game.orange_ghost_u
        self.right_img = game.orange_ghost_r
        self.left_image = game.orange_ghost_l

    def update(self, *args, **kwargs) -> None:
        if 1 < self.count_time <= 20:
            self.move(WIDTH-180, HEIGHT-180)
        elif self.count_time <= 40:
            self.scatter_model(WIDTH-180, HEIGHT-180)
        elif self.count_time == 60:
            self.origin_img = self.game.orange_ghost_d
            self.up_img = self.game.orange_ghost_u
            self.right_img = self.game.orange_ghost_r
            self.left_image = self.game.orange_ghost_l
            self.count_time = 0
        else:
            self.blue_module()
        self.count_time += 0.015625