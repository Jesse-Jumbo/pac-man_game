import random

from .SquareGrid import vec2int
from .collide_sprite_with_walls import collide_with_walls
from .settings import *
from .Ghost import Ghost


class OrangeGhost(Ghost):
    def __init__(self, game, x: float, y: float):
        super().__init__(game, x, y)
        self.image = game.ghosts_images[ORANGE_IMG][DOWN_IMG]
        self.origin_img = game.ghosts_images[ORANGE_IMG][DOWN_IMG]
        self.up_img = game.ghosts_images[ORANGE_IMG][UP_IMG]
        self.right_img = game.ghosts_images[ORANGE_IMG][RIGHT_IMG]
        self.left_image = game.ghosts_images[ORANGE_IMG][LEFT_IMG]
        self.go_out_limit = len(game.dots) + ORANGE_GO

    def chase_module(self):
        super().chase_module()
        self.orange_module()
