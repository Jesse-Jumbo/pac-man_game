import pygame.transform

from .setting import *


class Ghost(pygame.sprite.Sprite):
    def __init__(self, center_x=0, center_y=0):
        super().__init__()
        self.image = pygame.transform.scale(blue_ghost_d, (20, 25))
        self.rect = self.image.get_rect(center=(center_x, center_y))
        self.last_move = pygame.time.get_ticks()
        self.move_delay = 500

    def blue_module(self):
        origin_img = pygame.transform.scale(blue_ghost_d, (20, 25))
        up_img = pygame.transform.scale(blue_ghost_u, (20, 25))
        right_img = pygame.transform.scale(blue_ghost_r, (20, 25))
        left_image = pygame.transform.scale(blue_ghost_l, (20, 25))
        self.x_move = random.randrange(-3, 3)
        self.y_move = random.randrange(-3, 3)
        now = pygame.time.get_ticks()
        if now - self.last_move > self.move_delay:
            self.last_move = now
            old_center = self.image.get_rect()
            left_right_distance = self.rect.centerx - old_center.centerx
            up_down_distance = self.rect.centery - old_center.centery
            if abs(left_right_distance) > abs(up_down_distance):
                if left_right_distance >= 0:
                    self.image = right_img
                    print("r")
                else:
                    self.image = left_image
                    print("l")
            else:
                if up_down_distance <= 0:
                    self.image = origin_img
                    print("d")
                else:
                    self.image = up_img
                    print("u")
            self.rect.centerx += self.x_move
            self.rect.centery += self.y_move
            if self.rect.right >= WIDTH or self.rect.left <= 0:
                self.rect.centerx *= -1
            if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                self.rect.centery *= -1
