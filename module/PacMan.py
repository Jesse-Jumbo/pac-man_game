import pygame.math

from .collide_with_walls import collide_with_walls
from .setting import *


class PacMan(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        super().__init__(self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.origin_img = game.player_img
        self.up_img = game.up_img
        self.down_img = game.down_img
        self.turn_left_image = game.turn_left_image
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(x, y) * TILE_SIZE

    def update(self):
        self.get_keys()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt

        self.rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def get_keys(self):
        self.vel = pygame.math.Vector2(0, 0)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.image = self.game.up_img
            self.vel.y = -PLAYER_SPEED
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.image = self.game.down_img
            self.vel.y = PLAYER_SPEED
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.image = self.game.turn_left_image
            self.vel.x = -PLAYER_SPEED
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.image = self.game.player_img
            self.vel.x = PLAYER_SPEED
        # to slow the speed when move to corner
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071


    @property
    def player_data(self):
        return {
            "type": "rect",
            "name": "pac-man",
            "x": self.rect.x,
            "y": self.rect.y,
            "angle": 0,
            "width": self.rect.width,
            "height": self.rect.height,
        }
