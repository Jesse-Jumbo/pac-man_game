from mlgame.utils.enum import get_ai_name
from mlgame.view.view_model import create_image_view_data

from .TiledMap import Construction
from .env import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, construction: Construction, **kwargs):
        super().__init__()
        """
        初始化玩家資料
        construction可直接由TiledMap打包地圖資訊後傳入
        :param construction:
        :param kwargs:
        """
        self.id = construction.id
        self.no = construction.no
        self.rect = pygame.Rect(construction.init_pos, construction.init_size)
        self.play_rect_area = kwargs["play_rect_area"]
        self.size = construction.init_size
        self.angle = 0
        self.score = 0
        self.used_frame = 0
        self.lives = 3
        self.is_alive = True
        self.speed = PLAYER_SPEED
        self.dots_score = 0
        self.power_pellets_score = 0
        self.blue_ghosts_score = 0
        self.ate_dots_times = 0
        self.ate_power_pellets_times = 0
        self.ate_blue_ghosts_times = 0
        self.act_command = "right"
        self.image_index = 0
        self.index_control = 0
        self.is_move_up = False
        self.is_move_down = False
        self.is_move_left = False
        self.is_move_right = False

    def update(self, command: dict):
        self.used_frame += 1
        if self.lives <= 0:
            self.is_alive = False
            self.lives = 0

        if not self.is_alive:
            return

        if self.rect.right > self.play_rect_area.right \
                or self.rect.left < self.play_rect_area.left \
                or self.rect.bottom > self.play_rect_area.bottom \
                or self.rect.top < self.play_rect_area.top:
            self.collide_with_walls()
        else:
            self.act(command[get_ai_name(0)])

    def act(self, commands: list):
        if not commands:
            return None
        if self.is_move_right:
            self.move_right()
        elif self.is_move_left:
            self.move_left()
        elif self.is_move_up:
            self.move_up()
        elif self.is_move_down:
            self.move_down()
        if LEFT_CMD in commands:
            self.is_move_left = True
            self.is_move_up = False
            self.is_move_down = False
            self.is_move_right = False
        elif RIGHT_CMD in commands:
            self.is_move_right = True
            self.is_move_up = False
            self.is_move_down = False
            self.is_move_left = False
        elif UP_CMD in commands:
            self.is_move_up = True
            self.is_move_down = False
            self.is_move_left = False
            self.is_move_right = False
        elif DOWN_CMD in commands:
            self.is_move_down = True
            self.is_move_up = False
            self.is_move_left = False
            self.is_move_right = False

    def stop_move(self):
        self.is_move_left = not self.is_move_left if self.is_move_left else self.is_move_left
        self.is_move_up = not self.is_move_up if self.is_move_up else self.is_move_up
        self.is_move_down = not self.is_move_down if self.is_move_down else self.is_move_down
        self.is_move_right = not self.is_move_right if self.is_move_right else self.is_move_right

    def move_up(self):
        self.act_command = "up"
        self.rect.y += -self.speed

    def move_down(self):
        self.act_command = "down"
        self.rect.y += self.speed

    def move_left(self):
        self.act_command = "left"
        self.rect.x += -self.speed

    def move_right(self):
        self.act_command = "right"
        self.rect.x += self.speed

    def collide_with_walls(self):
        if self.is_move_right:
            self.move_left()
        elif self.is_move_left:
            self.move_right()
        elif self.is_move_up:
            self.move_down()
        elif self.is_move_down:
            self.move_up()
        self.stop_move()

    def collide_with_dots(self):
        self.score += DOT_SCORE
        self.ate_dots_times += 1
        self.dots_score += DOT_SCORE
        self.speed += -0.001

    def get_data_from_obj_to_game(self) -> dict:
        info = {"id": f"1P"
                , "x": self.rect.x
                , "y": self.rect.y
                , "speed": "{:.2f}".format(self.speed)
                , "score": self.score
                , "lives": self.lives
                , "dots_score": f"{self.dots_score}/{self.ate_dots_times} times"
                , "power_pellets_score": f"{self.power_pellets_score}/{self.ate_power_pellets_times} times"
                , "blue_ghosts_score": f"{self.blue_ghosts_score}/{self.ate_blue_ghosts_times} times"
                , "angle": self.angle
                }
        return info

    def get_obj_progress_data(self) -> dict:
        if not self.is_alive:
            return []
        self.index_control += 0.2
        self.image_index += int(self.index_control)
        if self.image_index >= 4:
            self.image_index = 0
        if self.index_control == 1:
            self.index_control = 0
        image_data = create_image_view_data(f"player_{self.act_command}_{self.image_index}", *self.rect.topleft,
                                            *self.size, self.angle
                                            )
        return image_data

    def get_info_to_game_result(self) -> dict:
        info = {"id": f"1P"
                , "x": self.rect.x
                , "y": self.rect.y
                , "speed": "{:.2f}".format(self.speed)
                , "score": self.score
                , "lives": self.lives
                , "dots_score": f"{self.dots_score}/{self.ate_dots_times} times"
                , "power_pellets_score": f"{self.power_pellets_score}/{self.ate_power_pellets_times} times"
                , "blue_ghosts_score": f"{self.blue_ghosts_score}/{self.ate_blue_ghosts_times} times"
                , "angle": self.angle
                }
        return info
