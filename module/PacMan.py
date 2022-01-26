import pygame.math

from .collide_hit_rect import collide_hit_rect
from .collide_sprite_with_walls import collide_with_walls
from .collide_player_with_ghosts import collide_player_with_ghosts
from .collide_sprite_with_nodes import collide_with_nodes
from .settings import *


class PacMan(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        super().__init__(self.groups)
        self.game = game
        self.present_player = 0
        self.image = game.player_images["right"][int(self.present_player)]
        self.right_img = self.game.player_images["right"]
        self.up_img = self.game.player_images["up"]
        self.down_img = self.game.player_images["down"]
        self.left_img = self.game.player_images["left"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect = PLAYRE_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(0, 0)
        self.pos.xy = self.rect.center
        self.node_pos = pygame.math.Vector2(self.rect.center) / TILE_SIZE

        self.speed = PLAYER_SPEED
        self.img_change_control = 0.4
        self.score = 0
        self.up_move = False
        self.down_move = False
        self.left_move = False
        self.right_move = False

    def update(self):
        self.present_player += self.img_change_control
        if self.present_player >= len(self.game.player_images["right"]):
            self.present_player = 0
        self.get_keys()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt

        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

        collide_player_with_ghosts(self, self.game.ghosts, WITH_GHOST)
        collide_with_nodes(self, self.game.nodes, 'node')

        hits = pygame.sprite.spritecollide(self, self.game.dots, True, collide_hit_rect)
        for hit in hits:
            self.score += DOT_SCORE
            self.speed += -0.1

        hits = pygame.sprite.spritecollide(self, self.game.points, True, collide_hit_rect)
        for hit in hits:
            self.score += POINT_SCORE
            self.game.player.score += POINT_SCORE
            self.game.red_ghost.blue_time()
            self.game.green_ghost.blue_time()
            self.game.pink_ghost.blue_time()
            self.game.orange_ghost.blue_time()
            self.game.danger = True
            self.game.music_play()

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
        if self.up_move:
            self.image = self.up_img[int(self.present_player)]
            self.vel.y = -self.speed
        if self.down_move:
            self.image = self.down_img[int(self.present_player)]
            self.vel.y = self.speed
        if self.left_move:
            self.image = self.left_img[int(self.present_player)]
            self.vel.x = -self.speed
        if self.right_move:
            self.image = self.right_img[int(self.present_player)]
            self.vel.x = self.speed
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
