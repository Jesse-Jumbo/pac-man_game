from .setting import *

class Dot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 0
        self.image = pygame.Surface([8, 8])
        self.color = YELLOW
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, 800)
        self.rect.centery = random.randint(0, 600)

    def update(self) -> None:
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

