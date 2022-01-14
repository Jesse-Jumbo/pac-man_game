from .collide_sprite_with_group import collide_with_walls
from .settings import *
from .Ghost import Ghost


class GreenGhost(Ghost):
    def __init__(self, game, img, x, y):
        super().__init__(game, img, x, y)
        self.image = img
        self.origin_img = game.green_ghost_images['down']
        self.up_img = game.green_ghost_images['up']
        self.right_img = game.green_ghost_images['right']
        self.left_image = game.green_ghost_images['left']
        self.go_out_limit = GREEN_GO

    def update(self, *args, **kwargs) -> None:
        pass
        # if self.is_out() and not self.is_blue:
        #     self.green__module()
        # else:
        #     self.frightened_module()
        #
        # self.rect.center = self.hit_rect.center
        # self.hit_rect.centerx = self.pos.x
        # collide_with_walls(self, self.game.walls, 'x')
        # self.hit_rect.centery = self.pos.y
        # collide_with_walls(self, self.game.walls, 'y')


