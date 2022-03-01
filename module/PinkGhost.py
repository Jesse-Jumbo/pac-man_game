from .settings import *
from games.pac_man.module.Ghost import Ghost


class PinkGhost(Ghost):
    def __init__(self, game, x: float, y: float):
        super().__init__(game, x, y)
        self.image = game.ghosts_images[PINK_IMG][DOWN_IMG]
        self.origin_img = game.ghosts_images[PINK_IMG][DOWN_IMG]
        self.up_img = game.ghosts_images[PINK_IMG][UP_IMG]
        self.right_img = game.ghosts_images[PINK_IMG][RIGHT_IMG]
        self.left_image = game.ghosts_images[PINK_IMG][LEFT_IMG]
        self.go_out_limit = len(game.dots) + PINK_GO

    def chase_module(self):
        super().chase_module()
        # pink ghost search player four front pos
        self.goal = pygame.math.Vector2(self.game.player.front_node_pos)

