from .env import *


class Node(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        super().__init__()
        self.rect = ALL_OBJECT_SIZE.copy()
        self.rect.x = x
        self.rect.y = y
        self.pos = pygame.math.Vector2(self.rect.center)
        self.pos_rect = NODE_HIT_RECT.copy()
        self.pos_rect.center = self.pos
