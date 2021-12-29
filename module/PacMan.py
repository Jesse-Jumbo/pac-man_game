from .setting import *

class PacMan(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        super().__init__(self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_x = 0
        self.speed_y = 0
        self.origin_img = game.player_img
        self.up_img = game.up_img
        self.down_img = game.down_img
        self.turn_left_image = game.turn_left_image

    def update(self):
        self.get_keys()
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def get_keys(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.image = self.game.up_img
            self.speed_y = -1
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.image = self.game.down_img
            self.speed_y = +1
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.image = self.game.turn_left_image
            self.speed_x = -1
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.image = self.game.player_img
            self.speed_x = +1

        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y




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
        }
