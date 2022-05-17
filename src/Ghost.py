import random
import pygame.transform

from GameFramework.Player import Player
from games.PacMan.src.SquareGrid import *

from .env import *


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
        self._move_cmd = random.choice([LEFT_cmd, RIGHT_cmd, UP_cmd, DOWN_cmd])
        self.move_change_frame = random.randrange(60, 610, 10)
        self.act_command = "right"

    def game_update(self, commands: str) -> None:
        if self.is_out:
            self.act(commands)
            if self.used_frame - self.blue_frame >= 600:
                self.is_blue = False
                self.blue_frame = 0
            if self.used_frame % self.move_change_frame == 0:
                self._move_cmd = random.choice([LEFT_cmd, RIGHT_cmd, UP_cmd, DOWN_cmd])
                self.move_change_frame = random.randrange(60, 610, 10)

    def act(self, commands: str):
        if self._move_cmd == LEFT_cmd:
            self.move_left()
        elif self._move_cmd == RIGHT_cmd:
            self.move_right()
        elif self._move_cmd == UP_cmd:
            self.move_up()
        elif self._move_cmd == DOWN_cmd:
            self.move_down()

    def get_info(self):
        if self.is_blue:
            if self._id == 5:
                id = "red_ghost"
            elif self._id == 4:
                id = "pink_ghost"
            elif self._id == 2:
                id = "green_ghost"
            elif self._id == 3:
                id = "orange_ghost"
        else:
            id = "blue_ghost"

        info = {"id": id, "x": self.rect.x, "y": self.rect.y}
        return info

    def collide_with_walls(self):
        self.vel *= -1
        self.rect.center += self.vel
        self._move_cmd = random.choice([UP_cmd, DOWN_cmd, LEFT_cmd, RIGHT_cmd])
        # if abs(self.vel.x) != 0:
        #     self._move_cmd = random.choice([UP_cmd, DOWN_cmd])
        # elif abs(self.vel.y) != 0:
        #     self._move_cmd = random.choice([LEFT_cmd, RIGHT_cmd])

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

    def enter_scatter_mode(self, x, y):
        pass

    def get_image_data(self):
        super().get_image_data()
        if not self.is_blue:
            if self._id == 5:
                _image_id = "red_ghost"
            elif self._id == 4:
                _image_id = "pink_ghost"
            elif self._id == 2:
                _image_id = "green_ghost"
            elif self._id == 3:
                _image_id = "orange_ghost"
        else:
            _image_id = "blue_ghost"
        image_data = {"id": f"{_image_id}_{self.act_command}", "x": self.rect.x, "y": self.rect.y,
                      "width": self.rect.width, "height": self.rect.height, "angle": 0}
        return image_data

    # TODO refactor draw path and search area
    # def draw_ghost_move_path(self, ghost):
    #     current = ghost.start  # + ghost.path[vec2int(ghost.start)]
    #     try:
    #         while vec2int(current) != vec2int(ghost.goal):# - ghost.path[vec2int(vec(list(ghost.path.keys())[1]))]:
    #             current += ghost.path[vec2int(current)]
    #             img = ghost.origin_img
    #             r = img.get_rect(center=(current.x * TILE_X_SIZE, current.y * TILE_Y_SIZE))
    #             self.window.blit(img, r)
    #     except (KeyError, IndexError):
    #         pass

    # def draw_search(self):
    #     # search area
    #     for node in self.path:
    #         x, y = node
    #         draw_rect = pygame.Rect(x * TILE_X_SIZE, y * TILE_Y_SIZE, TILE_X_SIZE, TILE_Y_SIZE)
    #         pygame.draw.rect(self.game.window, CYAN_BLUE, draw_rect, 1)
