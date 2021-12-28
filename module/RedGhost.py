import pygame.time

from .setting import *
from .Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(red_ghost_d, (20, 25))
        self.rect.center = [(WIDTH/2), (HEIGHT/2-17.5)]
        self.origin_img = pygame.transform.scale(red_ghost_d, (20, 25))
        self.up_img = pygame.transform.scale(red_ghost_u, (20, 25))
        self.right_img = pygame.transform.scale(red_ghost_r, (20, 25))
        self.left_image = pygame.transform.scale(red_ghost_l, (20, 25))

    def update(self, *args, **kwargs) -> None:
        if 1 < self.count_time <= 20:
            self.move(30, 30)
        elif self.count_time <= 40:
            self.scatter_model(30, 30)
        elif self.count_time >= 60:
            self.image = pygame.transform.scale(red_ghost_d, (20, 25))
            self.origin_img = pygame.transform.scale(red_ghost_d, (20, 25))
            self.up_img = pygame.transform.scale(red_ghost_u, (20, 25))
            self.right_img = pygame.transform.scale(red_ghost_r, (20, 25))
            self.left_image = pygame.transform.scale(red_ghost_l, (20, 25))
            self.count_time = 0
        else:
            self.blue_module()
        self.count_time += 0.015625
        print(self.count_time)





