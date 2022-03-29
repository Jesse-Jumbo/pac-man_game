import random
import pygame.transform

from games.PacMan.src.collide_hit_rect import collide_with_nodes, collide_with_walls
from games.PacMan.src.SquareGrid import *

from .env import *

def move():
    x_move = random.randrange(-3, 3)
    y_move = random.randrange(-3, 3)
    if x_move > y_move:
        return x_move
    return y_move


class Ghost(pygame.sprite.Sprite):
    # TODO refactor function name to (v)
    # TODO add state pattern
    def __init__(self, x: float, y: float):
        self._layer = GHOST_LAYER
        super().__init__()
        self.ghosts_images = {BLUE_IMG: {}, RED_IMG: {}, PINK_IMG: {}, GREEN_IMG: {}, ORANGE_IMG: {}}
        # TODO refactor img load mean
        for key, value, in blue_ghost_image_dic.items():
            self.ghosts_images[BLUE_IMG][key] = path.join(IMAGE_DIR, value)

        self.rect = ALL_OBJECT_SIZE.copy()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect = GHOST_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = pygame.math.Vector2(0, 0)
        self.pos.xy = self.rect.center
        self.blue_frame = 0
        self.frame = 0
        self.vel = pygame.math.Vector2(0, 0)
        self.speed = GHOST_SPEED
        self.blue_limit = BLUE_LIMIT
        self.speed_slow = SPEED_SLOW
        self.is_blue = False
        self.is_out = False
        self.draw_check_path = False
        self.get_blue_time = pygame.time.get_ticks()
        self.ghost_origin_pos = pygame.math.Vector2(0, 0)
        self.ghost_origin_pos.xy = self.rect.center

        self.node_pos = pygame.math.Vector2(self.rect.center) / TILE_SIZE
        self.last_search_time = pygame.time.get_ticks()

        self.origin_no = BLUE_GHOST_NO
        self.ghost_no = BLUE_GHOST_NO
        self.ghost_image_no = BLUE_IMG
        self.image_no = f"{self.ghost_no}_{DOWN_IMG}"
        self._move_cmd = random.choice([LEFT_cmd, RIGHT_cmd, UP_cmd, DOWN_cmd])

    def update(self, chase_path: list) -> None:
        self.frame += 1
        if self.is_out:
            if self._move_cmd == LEFT_cmd:
                self.move_left()
            elif self._move_cmd == RIGHT_cmd:
                self.move_right()
            elif self._move_cmd == UP_cmd:
                self.move_up()
            elif self._move_cmd == DOWN_cmd:
                self.move_down()

            if self.frame - self.blue_frame >= 1000:
                self.ghost_no = self.origin_no
                self.is_blue = False
                self.blue_frame = 0

            # if chase_path[-1].x == 1:
            #     self.move_right()
            # elif chase_path[-1].x == -1:
            #     self.move_left()
            # else:
            #     pass
            #
            # if chase_path[-1].y == -1:
            #     self.move_up()
            # elif chase_path[-1].y == 1:
            #     self.move_down()
            # else:
            #     pass

        self.rect.center = self.pos

        self.rect.center = self.hit_rect.center
        self.hit_rect.centerx = self.pos.x
        self.hit_rect.centery = self.pos.y

    def collide(self):
        self.vel *= -1
        self.pos += self.vel
        self.hit_rect.center = self.pos
        self.rect.center = self.pos
        self._move_cmd = random.choice([UP_cmd, DOWN_cmd, LEFT_cmd, RIGHT_cmd])
        # if abs(self.vel.x) != 0:
        #     self._move_cmd = random.choice([UP_cmd, DOWN_cmd])
        # elif abs(self.vel.y) != 0:
        #     self._move_cmd = random.choice([LEFT_cmd, RIGHT_cmd])
        self.pos += self.vel
        self.hit_rect.center = self.pos
        self.rect.center = self.pos

    def speed_up(self):
        pass
        # if len(self.game.dots) == len(self.game.dots) / 2:
        #     self.speed = self.speed * 1.1
        # if len(self.game.dots) == len(self.game.dots) / 3:
        #     self.speed = self.speed * 1.2

    def blue_time(self):
        self.blue_frame = self.frame
        self.ghost_no = BLUE_GHOST_NO
        self.is_blue = True

    def frightened_mode(self, grid):
        g = SquareGrid(grid, GRID_WIDTH, GRID_HEIGHT)
        # TODO define corner pos
        # escape_path = a_star_search(g, self.corner_pos, self.node_pos)
        escape_path = a_star_search(g, self.node_pos, self.node_pos)
        return escape_path

    def chase_mode(self, grid: pygame.sprite.Group, goal: vec):
        g = SquareGrid(grid, GRID_WIDTH, GRID_HEIGHT)
        chase_path = a_star_search(g, goal, self.node_pos)
        return chase_path

    def move_left(self):
        self.image_no = f"{self.ghost_no}_{LEFT_IMG}"
        if not self.is_blue:
            self.vel.x = -self.speed
        else:
            self.vel.x = -(self.speed + self.speed_slow)
        self.pos.x += self.vel.x

    def move_down(self):
        self.image_no = f"{self.ghost_no}_{DOWN_IMG}"
        if not self.is_blue:
            self.vel.y = self.speed
        else:
            self.vel.y = self.speed + self.speed_slow
        self.pos.y += self.vel.y

    def move_right(self):
        self.image_no = f"{self.ghost_no}_{RIGHT_IMG}"
        if not self.is_blue:
            self.vel.x = self.speed
        else:
            self.vel.x = self.speed + self.speed_slow
        self.pos.x += self.vel.x

    def move_up(self):
        self.image_no = f"{self.ghost_no}_{UP_IMG}"
        if not self.is_blue:
            self.vel.y = -self.speed
        else:
            self.vel.y = -(self.speed + self.speed_slow)
        self.pos.y += self.vel.y

    def scatter_mode(self, x, y):
        pass

    def get_position(self, xy: str):
        if xy == "x":
            return self.rect.x
        elif xy == "y":
            return self.rect.y
        else:
            return "please input x or y to get position"

    def get_info(self):
        return {
            "ghost_id": self.ghost_no,
            "pos_x": self.pos.x,
            "pos_y": self.pos.y,
        }

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
