import random

from .collide_sprite_with_group import collide_with_walls
from .settings import *
from .Ghost import Ghost


class OrangeGhost(Ghost):
    def __init__(self, game, img, x, y):
        super().__init__(game, img, x, y)
        self.image = img
        self.origin_img = game.orange_ghost_images['down']
        self.up_img = game.orange_ghost_images['up']
        self.right_img = game.orange_ghost_images['right']
        self.left_image = game.orange_ghost_images['left']
        self.go_out_limit = ORANGE_GO

    def update(self, *args, **kwargs) -> None:
        pass
        # if self.is_out() and not self.is_blue:
        #     self.orange_module()
        # elif self.is_blue:
        #     self.frightened_module()
        #
        # self.rect.center = self.hit_rect.center
        # self.hit_rect.centerx = self.pos.x
        # collide_with_walls(self, self.game.walls, 'x')
        # self.hit_rect.centery = self.pos.y
        # collide_with_walls(self, self.game.walls, 'y')

    def orange_module(self):
        self.origin_img = self.game.orange_ghost_images['down']
        self.up_img = self.game.orange_ghost_images['up']
        self.right_img = self.game.orange_ghost_images['right']
        self.left_image = self.game.orange_ghost_images['left']
        now = pygame.time.get_ticks()
        if now - self.last_move > self.move_delay:
            self.move_delay = random.randrange(5000, 10000)
            self.last_move = now
            self.target_pos.x = random.randrange(0+TILE_SIZE, WIDTH-TILE_SIZE)
            self.target_pos.y = random.randrange(0+TILE_SIZE, HEIGHT-TILE_SIZE)
            self.rot = (self.target_pos - self.pos).angle_to(pygame.math.Vector2(1, 0))
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