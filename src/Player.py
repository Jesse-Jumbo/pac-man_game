import pygame.math

from games.pac_man.src.collide_hit_rect import collide_hit_rect
from games.pac_man.src.collide_hit_rect import collide_with_walls, collide_player_with_ghosts, collide_with_nodes

from .env import *


class PacMan(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        self._layer = PLAYER_LAYER
        super().__init__()
        self.rect = pygame.Rect(x, y, all_object_size[0], all_object_size[1])
        self.state = True
        self.status = None
        self.player_no = 0
        self.pacman_info = {}
        self.used_frame = 0

        self.rect.x = x
        self.rect.y = y
        self.hit_rect = PLAYRE_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(0, 0)
        self.pos.xy = self.rect.center
        self.node_pos = pygame.math.Vector2(self.rect.center) / TILE_SIZE
        self.front_node_pos = self.node_pos

        self.speed = PLAYER_SPEED
        self.img_change_control = 0.4
        self.score = 0

    def move_up(self):
        self.vel.y = -self.speed
        self.front_node_pos.y = self.node_pos.y + -4

    def move_down(self):
        self.vel.y = self.speed
        self.front_node_pos.y = self.node_pos.y + 4

    def move_left(self):
        self.vel.x = -self.speed
        self.front_node_pos.x = self.node_pos.x + -4

    def move_right(self):
        self.vel.x = self.speed
        self.front_node_pos.x = self.node_pos.x + 4

    def keep_in_game(self, sprite_group: pygame.sprite.Group, dir: str):
        if dir == "walls":
            collide_with_walls(self, sprite_group, 'x')
            collide_with_walls(self, sprite_group, 'y')
        if dir == "ghosts":
            collide_player_with_ghosts(self, sprite_group)
        if dir == "nodes":
            collide_with_nodes(self, sprite_group)

    def get_info(self):
        self.pacman_info = {"id": self.player_no,
                            "pos": self.pos,
                            "status": self.status,
                            "velocity": self.vel,
                            "score": self.score}
        return self.pacman_info

    def handle_key_event(self, control_list: list):
        if control_list is None:
            return True
        if LEFT_cmd in control_list:
            self.move_left()
        if RIGHT_cmd in control_list:
            self.move_right()
        if UP_cmd in control_list:
            self.move_up()
        if DOWN_cmd in control_list:
            self.move_down()

    def update(self, control_list):
        if self.state:
            self.used_frame += 1
            self.handle_key_event(control_list)
            self.keep_in_game()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel

        self.hit_rect.centerx = self.pos.x
        self.hit_rect.centery = self.pos.y
        self.rect.center = self.hit_rect.center

        hits = pygame.sprite.spritecollide(self, self.game.dots, True, collide_hit_rect)
        for hit in hits:
            self.score += DOT_SCORE
            self.speed += -0.001

        hits = pygame.sprite.spritecollide(self, self.game.points, True, collide_hit_rect)
        for hit in hits:
            self.score += POINT_SCORE
            self.game.player.score += POINT_SCORE
            self.game.red_ghost.blue_time()
            self.game.pink_ghost.blue_time()
            self.game.green_ghost.blue_time()
            self.game.orange_ghost.blue_time()
            self.game.danger = True
            self.game.music_play()

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
