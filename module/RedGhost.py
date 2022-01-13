import pygame.time

from .collide_sprite_with_group import collide_with_walls, collide_with_nodes
from .settings import *
from .Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.red_ghost_images['down']
        self.origin_img = game.red_ghost_images['down']
        self.up_img = game.red_ghost_images['up']
        self.right_img = game.red_ghost_images['right']
        self.left_image = game.red_ghost_images['left']

    def update(self, *args, **kwargs) -> None:
        if self.is_out() and not self.is_blue and self.game.nodes:
            pass
            # collide_with_nodes(self, self.game.nodes, 'node')
            # collide_with_nodes(self, self.game.nodes, 'target')
            # self.red_module()
        else:
            self.frightened_module()

        self.move_up()
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

    def red_module(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(pygame.math.Vector2(1, 0))
        if -45 <= self.rot < 45:
            self.image = self.right_img
            self.vel.x = self.speed
            self.pos.x += self.vel.x * self.game.dt
        elif 45 <= self.rot < 135:
            self.image = self.up_img
            self.vel.y = -self.speed
            self.pos.y += self.vel.y * self.game.dt
        elif -135 >= self.rot or 180 >= self.rot >= 135:
            self.image = self.left_image
            self.vel.x = -self.speed
            self.pos.x += self.vel.x * self.game.dt
        else:
            self.image = self.origin_img
            self.vel.y = self.speed
            self.pos.y += self.vel.y * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.center = self.pos






