from .collide_sprite_with_walls import collide_with_walls
from .settings import *
from .Ghost import Ghost


class GreenGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.ghosts_images[GREEN_IMG][DOWN_IMG]
        self.origin_img = game.ghosts_images[GREEN_IMG][DOWN_IMG]
        self.up_img = game.ghosts_images[GREEN_IMG][UP_IMG]
        self.right_img = game.ghosts_images[GREEN_IMG][RIGHT_IMG]
        self.left_image = game.ghosts_images[GREEN_IMG][LEFT_IMG]
        self.go_out_limit = len(game.dots) + GREEN_GO

    def update(self, *args, **kwargs) -> None:
        if self.is_out():
            if not self.is_blue:
                self.green__module()
            elif self.is_blue:
                self.frightened_module()

        self.rect.center = self.hit_rect.center
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')


