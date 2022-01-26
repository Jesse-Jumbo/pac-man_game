from .SquareGrid import vec2int
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
        super().update()
        if self.is_out():
            if not self.is_blue:
                self.green__module()
            elif self.is_blue:
                self.frightened_module()

    def green__module(self):
        super().orange_module()
        try:
            if self.path[vec2int(self.start)].x == 1:
                self.move_right()
            elif self.path[vec2int(self.start)].y == -1:
                self.move_up()
            elif self.path[vec2int(self.start)].x == -1:
                self.move_left()
            elif self.path[vec2int(self.start)].y == 1:
                self.move_down()
        except KeyError:
            pass
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

