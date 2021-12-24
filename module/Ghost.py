from .setting import *


class Ghost(pygame.sprite.Sprite):
    def __init__(self, color=BLUE, center_x=0, center_y=0):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([20, 25])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(center_x, center_y))
        self.last_move = pygame.time.get_ticks()
        self.move_delay = 1000

    def blue_module(self):
        self.x_move = random.randrange(-50, 50)
        self.y_move = random.randrange(-50, 50)
        now = pygame.time.get_ticks()
        if now - self.last_move > self.move_delay:
            self.last_move = now
            self.rect.centerx += self.x_move
            self.rect.centery += self.y_move
            if self.rect.right >= WIDTH or self.rect.left <= 0:
                self.rect.centerx *= -1
            if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                self.rect.centery *= -1
