import pygame.time

from games.pac_man.src.Ghost import Ghost
from .env import *


class RedGhost(Ghost):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        for key, value, in red_ghost_image_dic.items():
            self.ghosts_images[RED_IMG][key] = pygame.image.load(path.join(IMAGE_DIR, value)).convert_alpha()
            image = self.ghosts_images[RED_IMG][key]
            self.ghosts_images[RED_IMG][key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

        self.image = self.ghosts_images[RED_IMG][DOWN_IMG]
        self.origin_img = self.ghosts_images[RED_IMG][DOWN_IMG]
        self.up_img = self.ghosts_images[RED_IMG][UP_IMG]
        self.right_img = self.ghosts_images[RED_IMG][RIGHT_IMG]
        self.left_image = self.ghosts_images[RED_IMG][LEFT_IMG]
        self.draw_rect = None
        self.update_time = pygame.time.get_ticks()
        self.ghost_no = RED_GHOST_NO

