import pygame.time

from .setting import *
from .Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.red_ghost_d
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.origin_img = game.red_ghost_d
        self.up_img = game.red_ghost_u
        self.right_img = game.red_ghost_r
        self.left_image = game.red_ghost_l
        self.game = game

    def update(self, *args, **kwargs) -> None:
        if 1 < self.count_time <= 20:
            self.move(30, 30)
        elif self.count_time <= 40:
            self.scatter_model(30, 30)
        elif self.count_time >= 60:
            self.image = self.game.green_ghost_d
            self.origin_img = self.game.green_ghost_d
            self.up_img = self.game.red_ghost_u
            self.right_img = self.game.red_ghost_r
            self.left_image = self.game.red_ghost_l
            self.count_time = 0
        else:
            self.blue_module()
        self.count_time += 0.015625
        print(self.count_time)





