from games.PacMan.src.Ghost import Ghost
from .env import *


class GreenGhost(Ghost):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.origin_no = GREEN_GHOST_NO
        self.ghost_no = GREEN_GHOST_NO
        self.ghost_image_no = GREEN_IMG
        for key, value, in green_ghost_image_dic.items():
            self.ghosts_images[GREEN_IMG][key] = path.join(IMAGE_DIR, value)

        self.image_no = f"{self.ghost_no}_{DOWN_IMG}"
        self.origin_img = f"{self.ghost_no}_{DOWN_IMG}"
        self.up_img = f"{self.ghost_no}_{UP_IMG}"
        self.right_img = f"{self.ghost_no}_{RIGHT_IMG}"
        self.left_image = f"{self.ghost_no}_{LEFT_IMG}"



