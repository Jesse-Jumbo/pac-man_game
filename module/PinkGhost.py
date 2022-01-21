from .collide_sprite_with_walls import collide_with_walls
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
        if self.is_out():
            if not self.is_blue:
                self.pink_module()
            elif self.is_blue:
                self.frightened_module()

        self.rect.center = self.hit_rect.center
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')

    def pink_module(self):
        self.origin_img = self.game.ghosts_images[PINK_IMG][DOWN_IMG]
        self.up_img = self.game.ghosts_images[PINK_IMG][UP_IMG]
        self.right_img = self.game.ghosts_images[PINK_IMG][RIGHT_IMG]
        self.left_image = self.game.ghosts_images[PINK_IMG][LEFT_IMG]
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
