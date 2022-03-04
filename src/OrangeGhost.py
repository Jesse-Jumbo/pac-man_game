from games.pac_man.src.Ghost import Ghost
from .env import *


class OrangeGhost(Ghost):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        for key, value, in orange_ghost_image_dic.items():
            self.ghosts_images[ORANGE_IMG][key] = pygame.image.load(path.join(IMAGE_DIR, value)).convert_alpha()
            image = self.ghosts_images[ORANGE_IMG][key]
            self.ghosts_images[ORANGE_IMG][key] = pygame.transform.scale(image, (TILE_X_SIZE, TILE_Y_SIZE))

        self.image = self.ghosts_images[ORANGE_IMG][DOWN_IMG]
        self.origin_img = self.ghosts_images[ORANGE_IMG][DOWN_IMG]
        self.up_img = self.ghosts_images[ORANGE_IMG][UP_IMG]
        self.right_img = self.ghosts_images[ORANGE_IMG][RIGHT_IMG]
        self.left_image = self.ghosts_images[ORANGE_IMG][LEFT_IMG]
        self.ghost_no = ORANGE_GHOST_NO
        self.img_name = orange_ghost_image_dic[DOWN_IMG]



