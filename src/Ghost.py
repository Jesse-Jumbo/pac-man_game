import random
import pygame.transform

from games.pac_man.src.collide_hit_rect import collide_with_nodes, collide_with_walls
from games.pac_man.src.SquareGrid import *

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
        for key, value, in blue_ghost_image_dic.items():
            self.ghosts_images[BLUE_IMG][key] = pygame.image.load(path.join(IMAGE_DIR, value)).convert_alpha()
            image = self.ghosts_images[BLUE_IMG][key]
            self.ghosts_images[BLUE_IMG][key] = pygame.transform.scale(image, (TILE_X_SIZE, TILE_Y_SIZE))

        self.image = self.ghosts_images[BLUE_IMG][DOWN_IMG]
        self.rect = ALL_OBJECT_SIZE.copy()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect = GHOST_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = pygame.math.Vector2(0, 0)
        self.pos.xy = self.rect.center
        self.origin_img = self.ghosts_images[BLUE_IMG][DOWN_IMG]
        self.up_img = self.ghosts_images[BLUE_IMG][UP_IMG]
        self.right_img = self.ghosts_images[BLUE_IMG][RIGHT_IMG]
        self.left_image = self.ghosts_images[BLUE_IMG][LEFT_IMG]
        self.blue_frame = 0
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

        self.ghost_no = BLUE_GHOST_NO
        self.img_name = blue_ghost_image_dic[DOWN_IMG]

    def update(self, chase_path: list) -> None:
        if self.is_out:

            if chase_path[-1].x == 1:
                self.move_right()
            elif chase_path[-1].x == -1:
                self.move_left()
            else:
                pass

            if chase_path[-1].y == -1:
                self.move_up()
            elif chase_path[-1].y == 1:
                self.move_down()
            else:
                pass

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.rect.center = self.hit_rect.center
        self.hit_rect.centerx = self.pos.x
        self.hit_rect.centery = self.pos.y

    def speed_up(self):
        pass
        # if len(self.game.dots) == len(self.game.dots) / 2:
        #     self.speed = self.speed * 1.1
        # if len(self.game.dots) == len(self.game.dots) / 3:
        #     self.speed = self.speed * 1.2

    def blue_time(self):
        self.blue_frame += 1
        if self.blue_frame >= 10000:
            self.is_blue = False
            self.blue_frame = 0
        else:
            self.is_blue = True

    def frightened_module(self, grid):
        g = SquareGrid(grid, GRID_WIDTH, GRID_HEIGHT)
        # TODO define corner pos
        # escape_path = a_star_search(g, self.corner_pos, self.node_pos)
        escape_path = a_star_search(g, self.node_pos, self.node_pos)
        return escape_path

    def chase_module(self, grid: pygame.sprite.Group, goal: vec):
        g = SquareGrid(grid, GRID_WIDTH, GRID_HEIGHT)
        chase_path = a_star_search(g, goal, self.node_pos)
        return chase_path

    def move_left(self):
        if not self.is_blue:
            self.image = self.left_image
            self.vel.x = -self.speed
        else:
            self.image = self.ghosts_images[BLUE_IMG][LEFT_IMG]
            self.vel.x = -(self.speed + self.speed_slow)
        self.pos.x += self.vel.x

    def move_down(self):
        if not self.is_blue:
            self.image = self.origin_img
            self.vel.y = self.speed
        else:
            self.image = self.ghosts_images[BLUE_IMG][DOWN_IMG]
            self.vel.y = self.speed + self.speed_slow
        self.pos.y += self.vel.y

    def move_right(self):
        if not self.is_blue:
            self.image = self.right_img
            self.vel.x = self.speed
        else:
            self.image = self.ghosts_images[BLUE_IMG][RIGHT_IMG]
            self.vel.x = self.speed + self.speed_slow
        self.pos.x += self.vel.x

    def move_up(self):
        if not self.is_blue:
            self.image = self.up_img
            self.vel.y = -self.speed
        else:
            self.image = self.ghosts_images[BLUE_IMG][UP_IMG]
            self.vel.y = -(self.speed + self.speed_slow)
        self.pos.y += self.vel.y

    def scatter_model(self, x, y):
        pass

    def get_position(self, xy: str):
        if xy == "x":
            return self.rect.x
        elif xy == "y":
            return self.rect.y
        else:
            return "please input x or y to get position"

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
