import pygame.transform

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
        pygame.sprite.Sprite.__init__(self, self.groups)
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

    def blue_module(self):
        x_move = random.randrange(-3, 3)
        y_move = random.randrange(-3, 3)
        now = pygame.time.get_ticks()
        if now - self.last_move > self.move_delay:
            self.last_move = now
            if self.rect.right >= WIDTH or self.rect.left <= 0:
                x_move *= -1
            if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                y_move *= -1
            if abs(x_move) > abs(y_move):
                if x_move >= 0:
                    self.image = self.right_img
                else:
                    self.image = self.left_image
            else:
                if y_move >= 0:
                    self.image = self.origin_img
                else:
                    self.image = self.up_img
            if x_move > y_move:
                self.rect.centerx += x_move
            elif y_move > x_move:
                self.rect.centery += y_move
            else:
                self.rect.centerx += x_move
                self.rect.centery += y_move

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
        self.rect.centerx += 1
        self.image = self.right_img

    def move_down(self):
        self.rect.centery += 1
        self.image = self.origin_img

    def move_left(self):
        self.rect.centerx += -1
        self.image = self.left_image

    def move_up(self):
        self.rect.centery += -1
        self.image = self.up_img
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


