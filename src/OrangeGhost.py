from games.PacMan.src.Ghost import Ghost
from .env import *


class OrangeGhost(Ghost):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.origin_no = ORANGE_GHOST_NO
        self.ghost_no = ORANGE_GHOST_NO
        self.ghost_image_no = ORANGE_IMG
        for key, value, in ORANGE_GHOST_IMAGE_PATH_DIC.items():
            self.ghosts_images[ORANGE_IMG][key] = path.join(IMAGE_DIR, value)

        self.image_no = f"{self.ghost_no}_{DOWN_IMG}"
        self.origin_img = f"{self.ghost_no}_{DOWN_IMG}"
        self.up_img = f"{self.ghost_no}_{UP_IMG}"
        self.right_img = f"{self.ghost_no}_{RIGHT_IMG}"
        self.left_image = f"{self.ghost_no}_{LEFT_IMG}"
        self.img_name = ORANGE_GHOST_IMAGE_PATH_DIC[DOWN_IMG]



