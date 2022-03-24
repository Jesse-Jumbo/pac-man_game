import pygame.time

from games.pac_man.src.Ghost import Ghost
from .env import *


class RedGhost(Ghost):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.origin_no = RED_GHOST_NO
        self.ghost_no = RED_GHOST_NO
        self.ghost_image_no = RED_IMG
        for key, value, in red_ghost_image_dic.items():
            self.ghosts_images[RED_IMG][key] = path.join(IMAGE_DIR, value)

        self.image_no = f"{self.ghost_no}_{DOWN_IMG}"
        self.origin_img = f"{self.ghost_no}_{DOWN_IMG}"
        self.up_img = f"{self.ghost_no}_{UP_IMG}"
        self.right_img = f"{self.ghost_no}_{RIGHT_IMG}"
        self.left_image = f"{self.ghost_no}_{LEFT_IMG}"
        self.draw_rect = None
        self.update_time = pygame.time.get_ticks()
        self.img_name = red_ghost_image_dic[DOWN_IMG]

