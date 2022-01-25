import pygame.transform

from .collide_player_with_ghosts import collide_player_with_ghosts
from .settings import *
from .SquareGrid import *


def move():
    x_move = random.randrange(-3, 3)
    y_move = random.randrange(-3, 3)
    if x_move > y_move:
        return x_move
    return y_move


class Ghost(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = GHOST_LAYER
        self.groups = game.all_sprites, game.ghosts
        super().__init__(self.groups)
        self.game = game
        self.image = game.ghosts_images[BLUE_IMG][DOWN_IMG]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect = GHOST_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = pygame.math.Vector2(0, 0)
        self.pos.xy = self.rect.center
        self.last_move = pygame.time.get_ticks()
        self.move_delay = 100
        self.origin_img = game.ghosts_images[BLUE_IMG][DOWN_IMG]
        self.up_img = game.ghosts_images[BLUE_IMG][UP_IMG]
        self.right_img = game.ghosts_images[BLUE_IMG][RIGHT_IMG]
        self.left_image = game.ghosts_images[BLUE_IMG][LEFT_IMG]
        self.rot = 0
        self.vel = pygame.math.Vector2(0, 0)
        self.speed = GHOST_SPEED
        self.target_pos = pygame.math.Vector2(0, 0)
        self.blue_limit = 10000
        self.speed_slow = SPEED_SLOW
        self.go_out_limit = len(game.dots) + RED_GO
        self.is_blue = False
        self.get_blue_time = pygame.time.get_ticks()
        self.ghost_origin_pos = pygame.math.Vector2(0, 0)
        self.ghost_origin_pos.xy = self.rect.center


        self.node_pos = pygame.math.Vector2(self.rect.center) / TILE_SIZE
        self.g = WeightedGrid(self.game, GRID_WIDTH, GRID_HEIGHT)
        self.goal = vec(self.game.player.node_pos)
        self.start = vec(self.node_pos)
        self.path, self.cost = a_star_search(self.g, self.goal, self.start)

    def is_out(self):
        if len(self.game.dots) <= self.go_out_limit:
            return True
        else:
            return False

    def blue_time(self):
        if self.is_out():
            self.get_blue_time = pygame.time.get_ticks()
            self.is_blue = True
            self.frightened_module()

    def frightened_module(self):
        if self.is_blue and self.is_out():
            now = pygame.time.get_ticks()
            collide_player_with_ghosts(self.game.player, self.game.ghosts, WITH_PLAYER)
            if now - self.get_blue_time > self.blue_limit:
                self.is_blue = False
            self.rot = (self.game.player.pos - self.pos).angle_to(pygame.math.Vector2(1, 0))
            if -45 <= self.rot < 45:
                self.image = self.game.ghosts_images[BLUE_IMG][LEFT_IMG]
                self.vel.x = -(self.speed + self.speed_slow)
                self.pos.x += self.vel.x * self.game.dt
            elif 45 <= self.rot < 135:
                self.image = self.game.ghosts_images[BLUE_IMG][DOWN_IMG]
                self.vel.y = self.speed + self.speed_slow
                self.pos.y += self.vel.y * self.game.dt
            elif -135 >= self.rot or 180 >= self.rot >= 135:
                self.image = self.game.ghosts_images[BLUE_IMG][RIGHT_IMG]
                self.vel.x = self.speed + self.speed_slow
                self.pos.x += self.vel.x * self.game.dt
            else:
                self.image = self.game.ghosts_images[BLUE_IMG][UP_IMG]
                self.vel.y = -(self.speed + self.speed_slow)
                self.pos.y += self.vel.y * self.game.dt
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

    def chase_module(self, dir:str):
        if dir == RED_MODULE:
            self.red_module()
        if dir == PINK_MODULE:
            self.pink_module()
        if dir == GREEN_MODULE:
            self.green__module()
        if dir == ORANGE_MODULE:
            self.orange_module()

    def orange_module(self):
        pass

    def green__module(self):
        pass

    def pink_module(self):
        pass

    def red_module(self):
        # red ghost search player
        self.g = WeightedGrid(self.game, GRID_WIDTH, GRID_HEIGHT)
        self.goal = vec(self.game.player.node_pos)
        self.start = vec(self.node_pos)
        self.path, self.cost = a_star_search(self.g, self.goal, self.start)

    def move_right(self):
        self.image = self.right_img
        self.vel.x = self.speed
        self.pos.x += self.vel.x * self.game.dt

    def move_down(self):
        self.image = self.origin_img
        self.vel.y = self.speed
        self.pos.y += self.vel.y * self.game.dt

    def move_left(self):
        self.image = self.left_image
        self.vel.x = -self.speed
        self.pos.x += self.vel.x * self.game.dt

    def move_up(self):
        self.image = self.up_img
        self.vel.y = -self.speed
        self.pos.y += self.vel.y * self.game.dt

    def scatter_model(self, x, y):
        pass

