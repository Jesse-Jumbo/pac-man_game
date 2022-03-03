import pygame.math

from .env import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        self._layer = PLAYER_LAYER
        super().__init__()
        self.player_images = []
        self.present_player = 0
        for i in ["cc", "c", "o", "oo"]:
            self.player_images.append(pygame.transform.scale(pygame.image.load(path.join(IMAGE_DIR, f"pac_man_{i}.png")).convert_alpha(), (TILE_SIZE, TILE_SIZE)))
        self.image = self.player_images[self.present_player]
        self.right_image = self.player_images
        self.rect = pygame.Rect(x, y, all_object_size[0], all_object_size[1])
        self.up_move = False
        self.down_move = False
        self.right_move = False
        self.left_move = False
        self.player_no = 0
        self.pacman_info = {}
        self.used_frame = 0

        self.hit_rect = pygame.Rect(x, y, object_hit_size[0], object_hit_size[1])
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(0, 0)
        self.pos.xy = self.rect.center
        self.node_pos = pygame.math.Vector2(self.rect.center) / TILE_SIZE
        self.front_node_pos = self.node_pos

        self.speed = PLAYER_SPEED
        self.img_change_control = 0.4
        self.score = 0

    def move_up(self):
        self.image = pygame.transform.rotate(self.right_image[self.present_player], 90)
        self.vel.y = -self.speed
        self.front_node_pos.y = self.node_pos.y + -4

    def move_down(self):
        self.image = pygame.transform.rotate(self.right_image[self.present_player], 270)
        self.vel.y = self.speed
        self.front_node_pos.y = self.node_pos.y + 4

    def move_left(self):
        self.image = pygame.transform.flip(self.right_image[self.present_player], True, False)
        self.vel.x = -self.speed
        self.front_node_pos.x = self.node_pos.x + -4

    def move_right(self):
        self.image = self.right_image[self.present_player]
        self.vel.x = self.speed
        self.front_node_pos.x = self.node_pos.x + 4

    def get_info(self):
        self.pacman_info = {"id": self.player_no,
                            "pos": self.pos,
                            "velocity": self.vel,
                            "score": self.score}
        return self.pacman_info

    def handle_key_event(self):
        if self.left_move:
            self.move_left()
        if self.right_move:
            self.move_right()
        if self.up_move:
            self.move_up()
        if self.down_move:
            self.move_down()

    def update(self, control_list):
        self.used_frame += 1
        self.present_player += self.img_change_control
        if self.present_player >= len(self.player_images):
            self.present_player = 0
        self.handle_key_event()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel

        self.hit_rect.centerx = self.pos.x
        self.hit_rect.centery = self.pos.y
        self.rect.center = self.hit_rect.center

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
        }
