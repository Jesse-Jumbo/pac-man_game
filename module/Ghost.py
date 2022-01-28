import random

import pygame.transform

from .collide_player_with_ghosts import collide_player_with_ghosts
from .collide_sprite_with_nodes import collide_with_nodes
from .collide_sprite_with_walls import collide_with_walls
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
        self.origin_img = game.ghosts_images[BLUE_IMG][DOWN_IMG]
        self.up_img = game.ghosts_images[BLUE_IMG][UP_IMG]
        self.right_img = game.ghosts_images[BLUE_IMG][RIGHT_IMG]
        self.left_image = game.ghosts_images[BLUE_IMG][LEFT_IMG]
        self.rot = 0
        self.vel = pygame.math.Vector2(0, 0)
        self.speed = GHOST_SPEED
        self.blue_limit = BLUE_LIMIT
        self.speed_slow = SPEED_SLOW
        self.go_out_limit = len(game.dots) + RED_GO
        self.is_blue = False
        self.draw_check_path = False
        self.get_blue_time = pygame.time.get_ticks()
        self.ghost_origin_pos = pygame.math.Vector2(0, 0)
        self.ghost_origin_pos.xy = self.rect.center

        self.node_pos = pygame.math.Vector2(self.rect.center) / TILE_SIZE
        self.g = SquareGrid(self.game.walls, GRID_WIDTH, GRID_HEIGHT)
        self.goal = vec(self.node_pos)
        self.start = vec(self.node_pos)
        self.path = a_star_search(self.g, self.goal, self.start)

        self.last_search_time = pygame.time.get_ticks()

    def update(self, *args, **kwargs) -> None:
        if self.is_out():
            self.check_path()
            self.frightened_module()
            self.chase_module()

        self.rect.center = self.hit_rect.center
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        collide_with_nodes(self, self.game.nodes, 'node')

    def speed_up(self):
        if len(self.game.dots) == len(self.game.dots) / 2:
            self.speed = self.speed * 1.1
        if len(self.game.dots) == len(self.game.dots) / 3:
            self.speed = self.speed * 1.2

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
        if self.is_blue:
            now = pygame.time.get_ticks()
            if now - self.get_blue_time > self.blue_limit:
                self.is_blue = False
            self.red_module()
            for path in self.path:
                if path.x == 1:
                    self.move_right()
                elif path.y == -1:
                    self.move_up()
                elif path.x == -1:
                    self.move_left()
                elif path.y == 1:
                    self.move_down()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

    def chase_module(self):
        for path in self.path:
            if path.x == 1:
                self.move_right()
            elif path.y == -1:
                self.move_up()
            elif path.x == -1:
                self.move_left()
            elif path.y == 1:
                self.move_down()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


    def orange_module(self):
        # orange ghost search a random pos
        if self.goal == self.start:
            node = vec(random.choice(list(self.game.node_pos)))
            self.goal = vec(node / TILE_SIZE)
        self.search()

    def green__module(self):
        # green ghost search random choice other module
        random.choice([self.red_module, self.pink_module, self.green__module, self.orange_module])()

    def pink_module(self):
        # pink ghost search player four front pos
        self.goal = vec(self.game.player.front_node_pos)
        self.search()

    def red_module(self):
        # red ghost search player
        self.goal = vec(self.game.player.node_pos)
        self.search()

    def search(self):
        self.start = vec(self.node_pos)
        now = pygame.time.get_ticks()
        if now - self.last_search_time > 0:
            self.path = a_star_search(self.g, self.goal, self.start)
            self.last_search_time = pygame.time.get_ticks()

    def move_left(self):
        if not self.is_blue:
            self.image = self.left_image
            self.vel.x = -self.speed
        else:
            self.image = self.game.ghosts_images[BLUE_IMG][LEFT_IMG]
            self.vel.x = -(self.speed + self.speed_slow)
        self.pos.x += self.vel.x * self.game.dt

    def move_down(self):
        if not self.is_blue:
            self.image = self.origin_img
            self.vel.y = self.speed
        else:
            self.image = self.game.ghosts_images[BLUE_IMG][DOWN_IMG]
            self.vel.y = self.speed + self.speed_slow
        self.pos.y += self.vel.y * self.game.dt

    def move_right(self):
        if not self.is_blue:
            self.image = self.right_img
            self.vel.x = self.speed
        else:
            self.image = self.game.ghosts_images[BLUE_IMG][RIGHT_IMG]
            self.vel.x = self.speed + self.speed_slow
        self.pos.x += self.vel.x * self.game.dt

    def move_up(self):
        if not self.is_blue:
            self.image = self.up_img
            self.vel.y = -self.speed
        else:
            self.image = self.game.ghosts_images[BLUE_IMG][UP_IMG]
            self.vel.y = -(self.speed + self.speed_slow)
        self.pos.y += self.vel.y * self.game.dt

    def scatter_model(self, x, y):
        pass

    def check_path(self):
        if self.draw_check_path:
            self.draw_search()
            self.draw_path()

    def draw_path(self):
        current = self.start  # + self.path[vec2int(self.start)]
        try:
            while vec2int(current) != vec2int(self.goal):# - self.path[vec2int(vec(list(self.path.keys())[1]))]:
                current += self.path[vec2int(current)]
                img = self.origin_img
                r = img.get_rect(center=(current.x * TILE_SIZE, current.y * TILE_SIZE))
                self.game.window.blit(img, r)
        except (KeyError, IndexError):
            pass

    def draw_search(self):
        # search area
        for node in self.path:
            x, y = node
            draw_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(self.game.window, CYAN_BLUE, draw_rect, 1)
