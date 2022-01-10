from .settings import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, walls, x, y, width, height):
        self.groups = walls
        super().__init__(self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, width, height)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
