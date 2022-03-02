from games.pac_man.module.settings import *


class Node(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        super().__init__()
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.pos_rect = pygame.Rect(x, y, 2, 2)
        self.pos_rect.center = self.pos
