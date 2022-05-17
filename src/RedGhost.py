import pygame.time

from games.PacMan.src.Ghost import Ghost
from .env import *


class RedGhost(Ghost):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.origin_no = RED_GHOST_NO
        self.ghost_no = RED_GHOST_NO
        self.ghost_image_no = RED_IMG
        for key, value, in RED_GHOST_IMAGE_PATH_DIC.items():
            self.ghosts_images[RED_IMG][key] = path.join(IMAGE_DIR, value)

        self.image_no = f"{self.ghost_no}_{DOWN_IMG}"
        self.origin_img = f"{self.ghost_no}_{DOWN_IMG}"
        self.up_img = f"{self.ghost_no}_{UP_IMG}"
        self.right_img = f"{self.ghost_no}_{RIGHT_IMG}"
        self.left_image = f"{self.ghost_no}_{LEFT_IMG}"
        self.draw_rect = False
        self.img_name = RED_GHOST_IMAGE_PATH_DIC[DOWN_IMG]

