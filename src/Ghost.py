import random

from games.PacMan.src.SquareGrid import *
from .env import *
from ...TankMan.GameFramework.Player import Player


class Ghost(Player):
    # TODO add state pattern
    def __init__(self, _id: int, _no: int, x: int, y: int, width: int, height: int):
        super().__init__(_id, _no, x, y, width, height)
        self.blue_frame = 0
        self.speed = GHOST_SPEED
        self.speed_slow = SPEED_SLOW
        self.is_blue = False
        self.is_out = False
        self.draw_check_path = False
        self._move_cmd = UP_cmd
        self.move_change_frame = random.randrange(60, 610, 10)
        self.act_command = "right"
        self.is_move_up = False
        self.is_move_down = False
        self.is_move_left = False
        self.is_move_right = False
        self.go_out_frame = 0

    def update_children(self):
        if self.used_frame > self.go_out_frame:
            self.is_out = True
        if self.is_out:
            if self.used_frame - self.blue_frame >= 600:
                self.is_blue = False
                self.blue_frame = 0
            if self.used_frame % self.move_change_frame == 0:
                self._move_cmd = random.choice([LEFT_cmd, RIGHT_cmd, UP_cmd, DOWN_cmd])
                self.move_change_frame = random.randrange(60, 610, 10)
            self.update_child()

    def update_child(self):
        """update this parent's child"""
        print("please overwrite this update")

    def act(self, commands: str):
        if self._move_cmd == LEFT_cmd:
            self.is_move_left = True
            self.is_move_up = False
            self.is_move_down = False
            self.is_move_right = False
            self.move_left()
        elif self._move_cmd == RIGHT_cmd:
            self.is_move_right = True
            self.is_move_up = False
            self.is_move_down = False
            self.is_move_left = False
            self.move_right()
        elif self._move_cmd == UP_cmd:
            self.is_move_up = True
            self.is_move_down = False
            self.is_move_left = False
            self.is_move_right = False
            self.move_up()
        elif self._move_cmd == DOWN_cmd:
            self.is_move_down = True
            self.is_move_up = False
            self.is_move_left = False
            self.is_move_right = False
            self.move_down()

    def collide_with_walls(self):
        self.vel *= -1
        self.rect.center += self.vel
        self._move_cmd = random.choice([UP_cmd, DOWN_cmd, LEFT_cmd, RIGHT_cmd])

    def get_blue_state(self):
        if self.is_out:
            self.blue_frame = self.used_frame
            self.is_blue = True

    def enter_frightened_mode(self, grid: pygame.sprite.Group):
        g = SquareGrid(grid, GRID_WIDTH, GRID_HEIGHT)
        # TODO define corner pos
        # escape_path = a_star_search(g, self.corner_pos, self.node_pos)
        escape_path = a_star_search(g, self.node_pos, self.node_pos)
        return escape_path

    def enter_chase_mode(self, grid: pygame.sprite.Group, goal: vec):
        g = SquareGrid(grid, GRID_WIDTH, GRID_HEIGHT)
        chase_path = a_star_search(g, goal, self.node_pos)
        return chase_path

    def move_left(self):
        self.act_command = "left"
        if not self.is_blue:
            self.vel.x = -self.speed
        else:
            self.vel.x = -(self.speed + self.speed_slow)
        self.rect.x += self.vel.x

    def move_down(self):
        self.act_command = "down"
        if not self.is_blue:
            self.vel.y = self.speed
        else:
            self.vel.y = self.speed + self.speed_slow
        self.rect.y += self.vel.y

    def move_right(self):
        self.act_command = "right"
        if not self.is_blue:
            self.vel.x = self.speed
        else:
            self.vel.x = self.speed + self.speed_slow
        self.rect.x += self.vel.x

    def move_up(self):
        self.act_command = "up"
        if not self.is_blue:
            self.vel.y = -self.speed
        else:
            self.vel.y = -(self.speed + self.speed_slow)
        self.rect.y += self.vel.y

    def collide_with_walls(self):
        if self.is_move_right:
            self._move_cmd = random.choice([UP_cmd, DOWN_cmd])
        elif self.is_move_left:
            self._move_cmd = random.choice([UP_cmd, DOWN_cmd])
        elif self.is_move_up:
            self._move_cmd = random.choice([LEFT_cmd, RIGHT_cmd])
        elif self.is_move_down:
            self._move_cmd = random.choice([LEFT_cmd, RIGHT_cmd])

    def enter_scatter_mode(self, x, y):
        pass
