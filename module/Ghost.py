from .setting import *


class Ghost(pygame.sprite.Sprite):
    def __init__(self, color=BLUE, centerx=0, centery=0):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([20, 25])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(centerx, centery))

    def blue_module(self):
        self.centerx = random.randrange(-5, 5)
        self.centery = random.randrange(-5, 5)
        self.rect.centerx += self.centerx
        self.rect.centery += self.centery
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.centerx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.centery *= -1
