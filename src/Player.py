import pygame.math

from mlgame.gamedev.game_interface import GameStatus
from .env import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        self._layer = PLAYER_LAYER
        super().__init__()
        self.player_no = 1
        self.image_dic = {}
        for key, value in PLAYER_IMG_DIC.items():
            self.image_dic[key] = path.join(IMAGE_DIR, value)
        self.image_path = f"player{self.player_no}P_{RIGHT_IMG}"
        self.present_player = 0
        self.rect = ALL_OBJECT_SIZE.copy()
        self.rect.x = x
        self.rect.y = y
        self.state = True
        # TODO to know what to do which self.status
        self.status = GameStatus.GAME_ALIVE
        self.up_move = False
        self.down_move = False
        self.right_move = False
        self.left_move = False
        self.pacman_info = {}
        self.result_info = {}
        self.used_frame = 0

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
        self.dots_score = 0
        self.power_pellets_score = 0
        self.blue_ghosts_score = 0
        self.ate_dots_times = 0
        self.ate_power_pellets_times = 0
        self.ate_blue_ghosts_times = 0

    def update(self, commands: dict):
        if self.state:
            self.used_frame += 1
            self.present_player += self.img_change_control
            # if self.present_player >= len(self.player_images):
            #     self.present_player = 0
            self.handle_key_event(commands)
            self.rect.center = self.pos

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

    def handle_key_event(self, commands: dict):
        if not commands[f"{self.player_no}P"]:
            return True
        else:
            if commands[f"{self.player_no}P"] == LEFT_cmd:
                self.move_left()
            elif commands[f"{self.player_no}P"] == RIGHT_cmd:
                self.move_right()
            elif commands[f"{self.player_no}P"] == UP_cmd:
                self.move_up()
            elif commands[f"{self.player_no}P"] == DOWN_cmd:
                self.move_down()

    def move_up(self):
        self.image_path = f"player{self.player_no}P_{UP_IMG}"
        self.vel.y = -self.speed
        self.front_node_pos.y = self.node_pos.y + -4
        self.pos.y += self.vel.y

    def move_down(self):
        self.image_path = f"player{self.player_no}P_{DOWN_IMG}"
        self.vel.y = self.speed
        self.front_node_pos.y = self.node_pos.y + 4
        self.pos.y += self.vel.y

    def move_left(self):
        self.image_path = f"player{self.player_no}P_{LEFT_IMG}"
        self.vel.x = -self.speed
        self.front_node_pos.x = self.node_pos.x + -4
        self.pos.x += self.vel.x

    def move_right(self):
        self.image_path = f"player{self.player_no}P_{RIGHT_IMG}"
        self.vel.x = self.speed
        self.front_node_pos.x = self.node_pos.x + 4
        self.pos.x += self.vel.x

    def get_info(self):
        self.pacman_info = {"player_id": f"{self.player_no}P",
                            "pos_x": int(self.pos.x),
                            "pos_y": int(self.pos.y),
                            "velocity": "{:.2f}".format(self.speed),
                            "score": self.score,
                            }
        return self.pacman_info

    def get_result(self):
        self.result_info = {"player_id": f"{self.player_no}P",
                            "pos_x": int(self.pos.x),
                            "pos_y": int(self.pos.y),
                            "velocity": "{:.2f}".format(self.speed),
                            "score": self.score,
                            "used_frame": self.used_frame,
                            "dots_score": f"{self.dots_score}/{self.ate_dots_times} times",
                            "power_pellets_score": f"{self.power_pellets_score}/{self.ate_power_pellets_times} times",
                            "blue_ghosts_score": f"{self.blue_ghosts_score}/{self.ate_blue_ghosts_times} times",
                            }
        return self.result_info

    def collide(self):
        self.vel *= -1
        self.pos += self.vel
        self.hit_rect.center = self.pos
        self.rect.center = self.pos

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

    def get_position(self, xy: str):
        if xy == "x":
            return self.rect.x
        elif xy == "y":
            return self.rect.y
        else:
            return "please input x or y to get position"
