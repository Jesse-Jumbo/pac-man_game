from .setting import *

class Dot(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self.group)
        self.image = pygame.Surface([8, 8])
        self.color = YELLOW
        self.rect = self.image.get_rect()
        self.rect.centerx = randm.randint(0, 800)
        self.rect.centery = randm.randint(0, 600)

    def update(self):
        self.angle += 10
        if self.angle > 360:
            self.angle -= 360

    @property
    def dot_data(self):
        return {
            "type": "rect",
            "name": "dot",
            "x": self.rect.x,
            "y": self.rect.y,
            "angle": 0,
            "width": self.rect.width,
            "height": self.rect.height,
            "color": self.color
        }