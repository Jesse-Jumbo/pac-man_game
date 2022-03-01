from .settings import *
from games.pac_man.module.Ghost import Ghost


class GreenGhost(Ghost):
    def __init__(self, game, x: float, y: float):
        super().__init__(game, x, y)
        self.image = game.ghosts_images[GREEN_IMG][DOWN_IMG]
        self.origin_img = game.ghosts_images[GREEN_IMG][DOWN_IMG]
        self.up_img = game.ghosts_images[GREEN_IMG][UP_IMG]
        self.right_img = game.ghosts_images[GREEN_IMG][RIGHT_IMG]
        self.left_image = game.ghosts_images[GREEN_IMG][LEFT_IMG]
        self.go_out_limit = len(game.dots) + GREEN_GO

    # def chase_module(self):
    #     super().chase_module()
    #     # green ghost search random choice other module
    #     random.choice([self.red_module, self.pink_module, self.green__module, self.orange_module])()


