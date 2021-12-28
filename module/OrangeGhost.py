from .setting import *
from .Ghost import Ghost


class OrangeGhost(Ghost):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(orange_ghost_d, (20, 25))
        self.rect.center = [(WIDTH/2+20), (HEIGHT/2+8)]
        self.origin_img = pygame.transform.scale(orange_ghost_d, (20, 25))
        self.up_img = pygame.transform.scale(orange_ghost_u, (20, 25))
        self.right_img = pygame.transform.scale(orange_ghost_r, (20, 25))
        self.left_image = pygame.transform.scale(orange_ghost_l, (20, 25))

    def update(self, *args, **kwargs) -> None:
        if 1 < self.count_time <= 20:
            self.move(WIDTH-180, HEIGHT-180)
        elif self.count_time <= 40:
            self.scatter_model(WIDTH-180, HEIGHT-180)
        elif self.count_time == 60:
            self.origin_img = pygame.transform.scale(orange_ghost_d, (20, 25))
            self.up_img = pygame.transform.scale(orange_ghost_u, (20, 25))
            self.right_img = pygame.transform.scale(orange_ghost_r, (20, 25))
            self.left_image = pygame.transform.scale(orange_ghost_l, (20, 25))
            self.count_time = 0
        else:
            self.blue_module()
        self.count_time += 0.015625