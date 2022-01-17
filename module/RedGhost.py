import pygame.time

from .collide_sprite_with_walls import collide_with_walls
from .collide_sprite_with_nodes import collide_with_nodes
from .settings import *
from .Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.red_ghost_images[DOWN_IMG]
        self.origin_img = game.red_ghost_images[DOWN_IMG]
        self.up_img = game.red_ghost_images[UP_IMG]
        self.right_img = game.red_ghost_images[RIGHT_IMG]
        self.left_image = game.red_ghost_images[LEFT_IMG]

    def update(self, *args, **kwargs) -> None:
        if self.is_out() and not self.is_blue:
            # collide_with_nodes(self, self.game.nodes, 'node')
            # collide_with_nodes(self, self.game.nodes, 'target')
            self.chase_module(RED_MODULE)
        else:
            self.frightened_module()
        #
        # self.move_up()
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

    def red_module(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(pygame.math.Vector2(1, 0))
        if -45 <= self.rot < 45:
            self.move_right()
        elif 45 <= self.rot < 135:
            self.move_up()
        elif -135 >= self.rot or 180 >= self.rot >= 135:
            self.move_left()
        else:
            self.move_down()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos






