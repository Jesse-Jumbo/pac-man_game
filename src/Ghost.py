import random

from mlgame.view.view_model import create_image_view_data

from .env import *


# TODO adjust blue settings
class Ghost(pygame.sprite.Sprite):
    # TODO add state pattern
    def __init__(self, construction, **kwargs):
        """
        初始化玩家資料
        construction可直接由TiledMap打包地圖資訊後傳入
        :param construction:
        :param kwargs:
        """
        super().__init__()
        self.image_id = "blue_ghost"
        self.id = construction.id
        self.no = construction.no
        self.rect = pygame.Rect(construction.init_pos, construction.init_size)
        self.origin_center = self.rect.center
        self.play_rect_area = kwargs["play_rect_area"]
        self.size = construction.init_size
        self.angle = 0
        self.score = 0
        self.used_frame = 0
        self.lives = 3
        self.is_alive = True
        self.blue_frame = 0
        self.speed = GHOST_SPEED
        self.speed_slow = SPEED_SLOW
        self.is_blue = False
        self.is_out = False
        self.draw_check_path = False
        self.move_cmd = UP_CMD
        self.move_change_frame = random.randrange(60, 610, 10)
        self.act_command = "right"
        self.is_move_up = False
        self.is_move_down = False
        self.is_move_left = False
        self.is_move_right = False
        self.go_out_frame = 0

    def update(self):
        self.used_frame += 1
        if self.lives <= 0:
            self.is_alive = False
            self.lives = 0
        if self.used_frame > self.go_out_frame:
            self.is_out = True
        if not self.is_alive or not self.is_out:
            return
        if self.used_frame - self.blue_frame >= 600:
            self.is_blue = False
            self.blue_frame = 0
        if self.used_frame % self.move_change_frame == 0:
            self.move_cmd = random.choice([LEFT_CMD, RIGHT_CMD, UP_CMD, DOWN_CMD])
            self.move_change_frame = random.randrange(60, 610, 10)
        if self.rect.right > self.play_rect_area.right \
                or self.rect.left < self.play_rect_area.left \
                or self.rect.bottom > self.play_rect_area.bottom \
                or self.rect.top < self.play_rect_area.top:
            self.collide_with_walls()
        else:
            self.act()

    def act(self):
        if self.move_cmd == LEFT_CMD:
            self.is_move_left = True
            self.is_move_up = False
            self.is_move_down = False
            self.is_move_right = False
            self.move_left()
        elif self.move_cmd == RIGHT_CMD:
            self.is_move_right = True
            self.is_move_up = False
            self.is_move_down = False
            self.is_move_left = False
            self.move_right()
        elif self.move_cmd == UP_CMD:
            self.is_move_up = True
            self.is_move_down = False
            self.is_move_left = False
            self.is_move_right = False
            self.move_up()
        elif self.move_cmd == DOWN_CMD:
            self.is_move_down = True
            self.is_move_up = False
            self.is_move_left = False
            self.is_move_right = False
            self.move_down()

    def get_blue_state(self):
        if self.is_out:
            self.blue_frame = self.used_frame
            self.is_blue = True

    def move_left(self):
        self.act_command = "left"
        if not self.is_blue:
            self.rect.x += -self.speed
        else:
            self.rect.x += -(self.speed + self.speed_slow)

    def move_down(self):
        self.act_command = "down"
        if not self.is_blue:
            self.rect.y += self.speed
        else:
            self.rect.y += self.speed + self.speed_slow

    def move_right(self):
        self.act_command = "right"
        if not self.is_blue:
            self.rect.x += self.speed
        else:
            self.rect.x += self.speed + self.speed_slow

    def move_up(self):
        self.act_command = "up"
        if not self.is_blue:
            self.rect.y += -self.speed
        else:
            self.rect.y += -(self.speed + self.speed_slow)

    def collide_with_walls(self):
        if self.is_move_right:
            self.move_left()
            self.move_cmd = random.choice([UP_CMD, DOWN_CMD])
        elif self.is_move_left:
            self.move_right()
            self.move_cmd = random.choice([UP_CMD, DOWN_CMD])
        elif self.is_move_up:
            self.move_down()
            self.move_cmd = random.choice([LEFT_CMD, RIGHT_CMD])
        elif self.is_move_down:
            self.move_up()
            self.move_cmd = random.choice([LEFT_CMD, RIGHT_CMD])
        self.act()

    def enter_scatter_mode(self, x, y):
        pass

    def get_data_from_obj_to_game(self) -> dict:
        info = {"id": f"{self.image_id}"
                , "x": self.rect.x
                , "y": self.rect.y
                , "speed": "{:.2f}".format(self.speed)
                , "act": self.act_command
                }
        return info

    def get_obj_progress_data(self) -> dict:
        if not self.is_alive:
            return []
        image_data = create_image_view_data(f"{self.image_id}_{self.act_command}", *self.rect.topleft,
                                            *self.size, self.angle
                                            )
        return image_data
