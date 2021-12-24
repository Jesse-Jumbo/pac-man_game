from .setting import *
from .Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y)
        self.image = pygame.transform.scale(red_ghost_d, (20, 25))
        origin_img = pygame.transform.scale(red_ghost_d, (20, 25))
        up_img = pygame.transform.scale(red_ghost_u, (20, 25))
        right_img = pygame.transform.scale(red_ghost_r, (20, 25))
        left_image = pygame.transform.scale(red_ghost_l, (20, 25))

    def update(self, *args, **kwargs) -> None:

        self.blue_module()
