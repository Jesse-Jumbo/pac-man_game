import pygame.time

from .collide_with_walls import collide_with_walls
from .setting import *
from .Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.red_ghost_d
        self.origin_img = game.red_ghost_d
        self.up_img = game.red_ghost_u
        self.right_img = game.red_ghost_r
        self.left_image = game.red_ghost_l

    def update(self, *args, **kwargs) -> None:
        self.red_move()
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        # if 1 < self.count_time <= 20:
        #     self.move(30, 30)
        # elif self.count_time <= 40:
        #     self.scatter_model(30, 30)
        # elif 20 < self.count_time <= 80:
        #     self.image = self.game.red_ghost_d
        #     self.origin_img = self.game.red_ghost_d
        #     self.up_img = self.game.red_ghost_u
        #     self.right_img = self.game.red_ghost_r
        #     self.left_image = self.game.red_ghost_l
        #     # self.count_time = 0
        # elif 80 < self.count_time <= 100:
        #     self.blue_module()
        # else:
        # self.count_time += 0.015625
        # print(self.count_time)

    def red_move(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(pygame.math.Vector2(1, 0))
        if -45 < self.rot < 45:
            self.image = self.game.red_ghost_r
            self.vel.x += 1
            self.pos.x += self.vel.x * self.game.dt
        elif 45 < self.rot < 135:
            self.image = self.game.red_ghost_u
            self.vel.y -= 1
            self.pos.y += self.vel.y * self.game.dt
        elif -135 > self.rot or 180 > self.rot > 135:
            self.image = self.game.red_ghost_l
            self.vel.x -= 1
            self.pos.x += self.vel.x * self.game.dt
        else:
            self.image = self.game.red_ghost_d
            self.vel.y += 1
            self.pos.y += self.vel.y * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.center = self.pos





