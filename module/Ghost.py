import pygame.transform

from .collide_sprite_with_group import ghost_collide
from .settings import *


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
        self.image = game.blue_ghost_images['down']
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = GHOST_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = pygame.math.Vector2(x, y)
        self.rect.center = self.pos
        self.last_move = pygame.time.get_ticks()
        self.move_delay = 100
        self.origin_img = game.blue_ghost_images['down']
        self.up_img = game.blue_ghost_images['up']
        self.right_img = game.blue_ghost_images['right']
        self.left_image = game.blue_ghost_images['left']
        self.count_time = 0
        self.game = game
        self.rot = 0
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)
        self.speed = GHOST_SPEED
        self.target_pos = pygame.math.Vector2(0, 0)
        self.blue_limit = 10000
        self.speed_slow = SPEED_SLOW
        self.go_out_limit = 100
        self.is_blue = False
        self.get_blue_time = pygame.time.get_ticks()
        self.move_left_or_right = [self.move_left(), self.move_right()]

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
            ghost_collide(self.game.player, self.game.ghosts, 'player')
            if now - self.get_blue_time > self.blue_limit:
                self.is_blue = False
            self.rot = (self.game.player.pos - self.pos).angle_to(pygame.math.Vector2(1, 0))
            if -45 <= self.rot < 45:
                self.image = self.game.blue_ghost_images['left']
                self.vel.x = -(GHOST_SPEED + self.speed_slow)
                self.pos.x += self.vel.x * self.game.dt
            elif 45 <= self.rot < 135:
                self.image = self.game.blue_ghost_images['down']
                self.vel.y = GHOST_SPEED + self.speed_slow
                self.pos.y += self.vel.y * self.game.dt
            elif -135 >= self.rot or 180 >= self.rot >= 135:
                self.image = self.game.blue_ghost_images['right']
                self.vel.x = GHOST_SPEED + self.speed_slow
                self.pos.x += self.vel.x * self.game.dt
            else:
                self.image = self.game.blue_ghost_images['up']
                self.vel.y = -(GHOST_SPEED + self.speed_slow)
                self.pos.y += self.vel.y * self.game.dt
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

    def chase_module(self):
        self.red_module()
        self.pink_module()
        self.green__module()
        self.orange_module()

    def orange_module(self):
        pass

    def green__module(self):
        pass

    def pink_module(self):
        pass

    def red_module(self):
        pass

    def move(self, x, y):
        if self.rect.centerx != x:
            if self.rect.centerx > x:
                self.move_left()
            else:
                self.move_right()
        elif self.rect.centery != y:
            if self.rect.centery > y:
                self.move_up()
            else:
                self.move_down()

    def move_right(self):
        self.image = self.right_img
        self.vel.x = GHOST_SPEED
        self.pos.x += self.vel.x * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x

    def move_down(self):
        self.image = self.origin_img
        self.vel.y = GHOST_SPEED
        self.pos.y += self.vel.y * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centery = self.pos.y

    def move_left(self):
        self.image = self.left_image
        self.vel.x = -GHOST_SPEED
        self.pos.x += self.vel.x * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x

    def move_up(self):
        self.image = self.up_img
        self.vel.y = -GHOST_SPEED
        self.pos.y += self.vel.y * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centery = self.pos.y

# TODO 改成任何情況下都能適用
    def scatter_model(self, x, y):
        if self.rect.centerx <= x+150 and self.rect.centery == y:
            self.move_right()
        if self.rect.centerx == x+150 and self.rect.centery <= y+150:
            self.move_down()
        if self.rect.centerx <= x+150 and self.rect.centery == y+150:
            self.move_left()
        if self.rect.centerx == x and self.rect.centery >= y:
            self.move_up()


