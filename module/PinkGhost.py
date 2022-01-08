from .collide_sprite_with_group import collide_with_walls
from .settings import *
from .Ghost import Ghost


class PinkGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.pink_ghost_images['down']
        self.origin_img = game.pink_ghost_images['down']
        self.up_img = game.pink_ghost_images['up']
        self.right_img = game.pink_ghost_images['right']
        self.left_image = game.pink_ghost_images['left']
        self.go_out_limit = PINK_GO

    def update(self, *args, **kwargs) -> None:
        if self.is_out() and not self.is_blue:
            self.pink_module()
        else:
            self.frightened_module()

        self.rect.center = self.hit_rect.center
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')

    def pink_module(self):
        self.origin_img = self.game.pink_ghost_images['down']
        self.up_img = self.game.pink_ghost_images['up']
        self.right_img = self.game.pink_ghost_images['right']
        self.left_image = self.game.pink_ghost_images['left']
        self.rot = (self.game.player.front_pos - self.pos).angle_to(pygame.math.Vector2(1, 0))
        if -45 <= self.rot < 45:
            self.image = self.right_img
            self.vel.x = GHOST_SPEED
            self.pos.x += self.vel.x * self.game.dt
        elif 45 <= self.rot < 135:
            self.image = self.up_img
            self.vel.y = -GHOST_SPEED
            self.pos.y += self.vel.y * self.game.dt
        elif -135 >= self.rot or 180 >= self.rot >= 135:
            self.image = self.left_image
            self.vel.x = -GHOST_SPEED
            self.pos.x += self.vel.x * self.game.dt
        else:
            self.image = self.origin_img
            self.vel.y = GHOST_SPEED
            self.pos.y += self.vel.y * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
