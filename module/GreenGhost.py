from .collide_sprite_with_group import collide_with_walls
from .settings import *
from .Ghost import Ghost


class GreenGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.green_ghost_images['down']
        self.origin_img = game.green_ghost_images['down']
        self.up_img = game.green_ghost_images['up']
        self.right_img = game.green_ghost_images['right']
        self.left_image = game.green_ghost_images['left']

    def update(self, *args, **kwargs) -> None:
        if len(self.game.dots) < 70:
            self.hit_rect.centerx = self.pos.x
            collide_with_walls(self, self.game.walls, 'x')
            self.hit_rect.centery = self.pos.y
            collide_with_walls(self, self.game.walls, 'y')
            self.rect.center = self.hit_rect.center
            if self.is_blue:
                self.blue_module()
            else:
                pass

