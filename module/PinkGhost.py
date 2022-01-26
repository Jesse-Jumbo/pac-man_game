from .SquareGrid import vec2int
from .settings import *
from .Ghost import Ghost


class PinkGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.ghosts_images[PINK_IMG][DOWN_IMG]
        self.origin_img = game.ghosts_images[PINK_IMG][DOWN_IMG]
        self.up_img = game.ghosts_images[PINK_IMG][UP_IMG]
        self.right_img = game.ghosts_images[PINK_IMG][RIGHT_IMG]
        self.left_image = game.ghosts_images[PINK_IMG][LEFT_IMG]
        self.go_out_limit = len(game.dots) + PINK_GO

    def update(self, *args, **kwargs) -> None:
        super().update()
        if self.is_out():
            if not self.is_blue:
                self.pink_module()
            elif self.is_blue:
                self.frightened_module()


    def pink_module(self):
        super().pink_module()
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
