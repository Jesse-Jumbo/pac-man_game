import math

import pygame.time

from .SquareGrid import vec2int
from .settings import *
from .Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self, game, x: float, y: float):
        super().__init__(game, x, y)
        self.image = game.ghosts_images[RED_IMG][DOWN_IMG]
        self.origin_img = game.ghosts_images[RED_IMG][DOWN_IMG]
        self.up_img = game.ghosts_images[RED_IMG][UP_IMG]
        self.right_img = game.ghosts_images[RED_IMG][RIGHT_IMG]
        self.left_image = game.ghosts_images[RED_IMG][LEFT_IMG]
        self.draw_rect = None
        self.update_time = pygame.time.get_ticks()

    def chase_module(self):
        super().chase_module()
        # red ghost search player
        self.goal = pygame.math.Vector2(self.game.player.node_pos)

