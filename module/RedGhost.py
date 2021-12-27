import pygame.time

from .setting import *
from .Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y)
        self.image = pygame.transform.scale(red_ghost_d, (20, 25))
        self.origin_img = pygame.transform.scale(red_ghost_d, (20, 25))
        self.up_img = pygame.transform.scale(red_ghost_u, (20, 25))
        self.right_img = pygame.transform.scale(red_ghost_r, (20, 25))
        self.left_image = pygame.transform.scale(red_ghost_l, (20, 25))

    def update(self, *args, **kwargs) -> None:
        if self.count_time <= 1200:
            self.move(30, 30)
        elif self.count_time <= 2400:
            self.scatter_model(30, 30)
        elif self.count_time >= 3600:
            self.image = pygame.transform.scale(red_ghost_d, (20, 25))
            self.origin_img = pygame.transform.scale(red_ghost_d, (20, 25))
            self.up_img = pygame.transform.scale(red_ghost_u, (20, 25))
            self.right_img = pygame.transform.scale(red_ghost_r, (20, 25))
            self.left_image = pygame.transform.scale(red_ghost_l, (20, 25))
            self.count_time = 0
        else:
            self.blue_module()
        self.count_time += 1
        print(self.count_time)





