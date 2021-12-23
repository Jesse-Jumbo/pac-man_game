from setting import *


class PacMan(pygame.sprite.Sprite):
    def __init__(self, color=YELLOW):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.centery = 400

    def update(self):
        if motion == "UP":
            self.rect.centery -= 10
        elif motion == "DOWN":
            self.rect.centery += 10
        elif motion == "LEFT":
            self.rect.centerx -= 10
        elif motion == "RIGHT":
            self.rect.centerx += 10

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