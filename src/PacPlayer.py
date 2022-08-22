from .env import *
from games.TankMan.src.GameFramework.Player import Player

vec = pygame.math.Vector2


class PacPlayer(Player):
    def __init__(self, construction, **kwargs):
        super().__init__(construction, **kwargs)
        self.up_move = False
        self.down_move = False
        self.right_move = False
        self.left_move = False
        self.speed = PLAYER_SPEED
        self.dots_score = 0
        self.power_pellets_score = 0
        self.blue_ghosts_score = 0
        self.ate_dots_times = 0
        self.ate_power_pellets_times = 0
        self.ate_blue_ghosts_times = 0
        # TODO rename
        self.act_command = "right"
        self.image_index = 0
        self.index_control = 0
        self.is_move_up = False
        self.is_move_down = False
        self.is_move_left = False
        self.is_move_right = False

    def update_children(self):
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def act(self, commands: str):
        if commands == LEFT_cmd:
            self.is_move_left = True
            self.is_move_up = False
            self.is_move_down = False
            self.is_move_right = False
            self.move_left()
        elif commands == RIGHT_cmd:
            self.is_move_right = True
            self.is_move_up = False
            self.is_move_down = False
            self.is_move_left = False
            self.move_right()
        elif commands == UP_cmd:
            self.is_move_up = True
            self.is_move_down = False
            self.is_move_left = False
            self.is_move_right = False
            self.move_up()
        elif commands == DOWN_cmd:
            self.is_move_down = True
            self.is_move_up = False
            self.is_move_left = False
            self.is_move_right = False
            self.move_down()

    def get_info(self):
        info = {"id": f"Player",
                "x": self.rect.x,
                "y": self.rect.y,
                "speed": "{:.2f}".format(self.speed),
                "score": self.score,
                "lives": self.lives,
                "dots_score": f"{self.dots_score}/{self.ate_dots_times} times",
                "power_pellets_score": f"{self.power_pellets_score}/{self.ate_power_pellets_times} times",
                "blue_ghosts_score": f"{self.blue_ghosts_score}/{self.ate_blue_ghosts_times} times"
                }
        return info

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

    def collide_with_dots(self):
        self.score += DOT_SCORE
        self.ate_dots_times += 1
        self.dots_score += DOT_SCORE
        self.speed += -0.001

    def get_image_data(self):
        self.index_control += 0.2
        self.image_index += int(self.index_control)
        if self.image_index >= 4:
            self.image_index = 0
        if self.index_control == 1:
            self.index_control = 0
        image_data = {"id": f"player_{self.act_command}_{self.image_index}", "x": self.rect.x, "y": self.rect.y,
                      "width": self.rect.width, "height": self.rect.height, "angle": 0}
        return image_data
