import pygame

from .setting import *


class PacMan(pygame.sprite.Sprite):
    def __init__(self, color=YELLOW):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 300
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.speed_y = -3
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.speed_y = +3
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speed_x = -3
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speed_x = +3

        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


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
            "color": self.color
        }
