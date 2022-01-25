import math

import pygame.time

from .SquareGrid import vec2int
from .collide_sprite_with_walls import collide_with_walls
from .collide_sprite_with_nodes import collide_with_nodes
from .settings import *
from .Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.ghosts_images[RED_IMG][DOWN_IMG]
        self.origin_img = game.ghosts_images[RED_IMG][DOWN_IMG]
        self.up_img = game.ghosts_images[RED_IMG][UP_IMG]
        self.right_img = game.ghosts_images[RED_IMG][RIGHT_IMG]
        self.left_image = game.ghosts_images[RED_IMG][LEFT_IMG]
        self.draw_rect = None
        self.update_time = pygame.time.get_ticks()
        self.node_pos = pygame.math.Vector2(self.rect.center) / TILE_SIZE

    def update(self, *args, **kwargs) -> None:
        if self.is_out() and not self.is_blue:
            self.chase_module(RED_MODULE)
        elif self.is_out() and self.is_blue:
            self.frightened_module()

        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

        collide_with_nodes(self, self.game.nodes, 'node')

    def red_module(self):
        try:
            if self.game.path[vec2int(self.game.start)].x == 1:
                self.move_right()
            elif self.game.path[vec2int(self.game.start)].y == -1:
                self.move_up()
            elif self.game.path[vec2int(self.game.start)].x == -1:
                self.move_left()
            elif self.game.path[vec2int(self.game.start)].y == 1:
                self.move_down()
        except KeyError:
            pass
        self.rect = self.image.get_rect()
        self.rect.center = self.pos




