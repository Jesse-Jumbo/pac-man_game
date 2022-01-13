import pygame.math

from .collide_sprite_with_group import collide_with_walls, ghost_collide, collide_with_nodes
from .settings import *


class PacMan(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        super().__init__(self.groups)
        self.game = game
        self.present_player = 0
        self.image = game.player_right_images[self.present_player]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = PLAYRE_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(x, y)
        self.right_img = game.player_right_images[int(self.present_player)]
        self.up_img = game.player_up_images[int(self.present_player)]
        self.down_img = game.player_down_images[int(self.present_player)]
        self.left_img = game.player_left_images[int(self.present_player)]
        self.front_pos = pygame.math.Vector2(self.rect.centerx, self.rect.centery)
        self.img_change_control = 0.4
        self.node_value = 0
        self.node_pos = pygame.math.Vector2(0, 0)

    def update(self):
        self.present_player += self.img_change_control
        if self.present_player >= len(self.game.player_right_images):
            self.present_player = 0
        self.get_keys()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt

        self.hit_rect.centerx = self.pos.x
        # collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        # collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

        ghost_collide(self, self.game.ghosts, 'ghost')
        collide_with_nodes(self, self.game.nodes, 'update_node')



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
            self.image = self.game.player_up_images[int(self.present_player)]
            self.vel.y = -PLAYER_SPEED
            self.front_pos = (self.rect.centerx, self.rect.top - TILE_SIZE)
        elif keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.image = self.game.player_down_images[int(self.present_player)]
            self.vel.y = PLAYER_SPEED
            self.front_pos = (self.rect.centerx, self.rect.bottom + TILE_SIZE)
        elif keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.image = self.game.player_left_images[int(self.present_player)]
            self.vel.x = -PLAYER_SPEED
            self.front_pos = (self.rect.left - TILE_SIZE, self.rect.centery)
        elif keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.image = self.game.player_right_images[int(self.present_player)]
            self.vel.x = PLAYER_SPEED
            self.front_pos = (self.rect.right + TILE_SIZE, self.rect.centery)
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
