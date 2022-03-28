from .env import *
from games.PacMan.src.Ghost import Ghost


class PinkGhost(Ghost):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.origin_no = PINK_GHOST_NO
        self.ghost_no = PINK_GHOST_NO
        self.ghost_image_no = PINK_IMG
        for key, value, in pink_ghost_image_dic.items():
            self.ghosts_images[PINK_IMG][key] = path.join(IMAGE_DIR, value)

        self.image_no = f"{self.ghost_no}_{DOWN_IMG}"
        self.origin_img = f"{self.ghost_no}_{DOWN_IMG}"
        self.up_img = f"{self.ghost_no}_{UP_IMG}"
        self.right_img = f"{self.ghost_no}_{RIGHT_IMG}"
        self.left_image = f"{self.ghost_no}_{LEFT_IMG}"
        self.img_name = pink_ghost_image_dic[DOWN_IMG]




