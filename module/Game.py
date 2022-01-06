import sys

import pygame.event

from .Obstacle import Obstacle
from .TiledMap import TiledMap
from .draw_text import draw_text
from .settings import *
from .PacMan import PacMan
from .Dot import Dot
from .Point import Point
from .RedGhost import RedGhost
from .GreenGhost import GreenGhost
from .PinkGhost import PinkGhost
from .OrangeGhost import OrangeGhost
from .Wall import Wall
from .Map import Map


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        # pygame.key.set_repeat(500, 100)
        self.load_data()

        self.score = 0
        self.show_start_screen()

    def load_data(self):
        """folder path"""
        game_dir = path.dirname(__file__)
        img_dir = path.join(game_dir, '../img')
        snd_dir = path.join(game_dir, '../snd')
        map_dir = path.join(game_dir, '../maps')
        '''font'''
        self.font_name = pygame.font.match_font('arial')
        '''stop window'''
        self.dim_window = pygame.Surface(self.window.get_size()).convert_alpha()
        self.dim_window.fill((0, 0, 0, 100))
        '''load map'''
        for i in range(2, 3):
            self.map = TiledMap(path.join(map_dir, f'map0{i}.tmx'))
            self.map_img = self.map.make_map()
            self.map_rect = self.map_img.get_rect()

        """img"""
        """wall"""
        self.wall_img = pygame.image.load(path.join(img_dir, WALL_IMG)).convert_alpha()
        self.wall_img = pygame.transform.scale(self.wall_img, (TILE_SIZE, TILE_SIZE))
        """player"""
        self.player_img = pygame.image.load(path.join(img_dir, PLAYER_IMG)).convert_alpha()
        self.player_img = pygame.transform.scale(self.player_img, (TILE_SIZE, TILE_SIZE))
        self.up_img = pygame.transform.scale((pygame.transform.rotate(self.player_img, 90)), (TILE_SIZE, TILE_SIZE))
        self.down_img = pygame.transform.scale((pygame.transform.rotate(self.player_img, 270)), (TILE_SIZE, TILE_SIZE))
        self.turn_left_image = pygame.transform.scale((pygame.transform.flip(self.player_img, True, False)), (TILE_SIZE, TILE_SIZE))
        """dot"""
        self.small_dot_img = pygame.image.load(path.join(img_dir, DOT_IMG)).convert_alpha()
        self.big_dot_img = pygame.image.load(path.join(img_dir, POINT_IMG)).convert_alpha()
        self.small_dot_img = pygame.transform.scale(self.small_dot_img, (8, 8))
        self.big_dot_img = pygame.transform.scale(self.big_dot_img, (20, 20))
        """blue ghost"""
        self.blue_ghost_images = {}
        for key, value, in blue_ghost_image_dic.items():
            self.blue_ghost_images[key] = pygame.image.load(path.join(img_dir, value)).convert_alpha()
            image = self.blue_ghost_images[key]
            self.blue_ghost_images[key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        """green ghost"""
        self.green_ghost_images = {}
        for key, value, in green_ghost_image_dic.items():
            self.green_ghost_images[key] = pygame.image.load(path.join(img_dir, value)).convert_alpha()
            image = self.green_ghost_images[key]
            self.green_ghost_images[key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        """red ghost"""
        self.red_ghost_images = {}
        for key, value, in red_ghost_image_dic.items():
            self.red_ghost_images[key] = pygame.image.load(path.join(img_dir, value)).convert_alpha()
            image = self.red_ghost_images[key]
            self.red_ghost_images[key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        """pink ghost"""
        self.pink_ghost_images = {}
        for key, value, in pink_ghost_image_dic.items():
            self.pink_ghost_images[key] = pygame.image.load(path.join(img_dir, value)).convert_alpha()
            image = self.pink_ghost_images[key]
            self.pink_ghost_images[key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        """orange ghost"""
        self.orange_ghost_images = {}
        for key, value, in orange_ghost_image_dic.items():
            self.orange_ghost_images[key] = pygame.image.load(path.join(img_dir, value)).convert_alpha()
            image = self.orange_ghost_images[key]
            self.orange_ghost_images[key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

    def new(self):
        # initialize all variables and so all the setup for a new game
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        #
        # self.all_sprites.add(self.player)
        # #
        for i in range(100):
            Dot(self)
        # #
        # Point(self, 30, 30)
        # #
        # Point(self, WIDTH - 30, 30)
        # #
        # Point(self, 30, HEIGHT - 30)
        # #
        # Point(self, WIDTH - 30, HEIGHT - 30)
        #
        # Wall
        # for row, tiles in enumerate(self.map.map_data):
        #     for col, tile in enumerate(tiles):
        #         if tile == '1':
        #             wall = Wall(self, col, row)
        #             self.walls.add(wall)
        #         if tile == 'p':
        #             self.player = PacMan(self, col, row)
        for tile_object in self.map.tmxdata.objects:
            obj_center = pygame.math.Vector2(tile_object.x + tile_object.width / 2,
                                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = PacMan(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'red_ghost':
                self.red_ghost = RedGhost(self, obj_center.x, obj_center.y)
            if tile_object.name == 'green_ghost':
                GreenGhost(self, obj_center.x, obj_center.y)
            if tile_object.name == 'pink_ghost':
                PinkGhost(self, obj_center.x, obj_center.y)
            if tile_object.name == 'orange_ghost':
                OrangeGhost(self, obj_center.x, obj_center.y)
            if tile_object.name == 'point':
                Point(self, obj_center.x, obj_center.y)
        self.draw_debug = False
        self.paused = False


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            if not self.paused:
                self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # update potion of the game loop
        self.all_sprites.update()
        # game over?
        if len(self.dots) == 0 and self.dt != 0:
            self.playing = False
            self.show_win_screen()

        hits = pygame.sprite.spritecollide(self.player, self.dots, True)
        for hit in hits:
            self.score += 10

        hits = pygame.sprite.spritecollide(self.player, self.points, True)
        for hit in hits:
            self.score += 50

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.window, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.window, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pygame.display.set_caption(TITLE+"{:.2f}".format(self.clock.get_fps()))
        # self.window.fill(BG_COLOR)
        self.window.blit(self.map_img, self.map_rect)
        # self.draw_grid()
        draw_text(self.window, str(self.score), self.font_name, 30, WHITE,  WIDTH / 2, 10, "n")
        for sprite in self.all_sprites:
            self.window.blit(sprite.image, sprite.rect)
            if self.draw_debug:
                pygame.draw.rect(self.window, CYAN_BLUE, sprite.rect, 1)
        if self.draw_debug:
            for wall in self.walls:
                pygame.draw.rect(self.window, CYAN_BLUE, wall.rect, 1)
            for ghost in self.ghosts:
                pygame.draw.rect(self.window, CYAN_BLUE, ghost.hit_rect, 1)
            pygame.draw.rect(self.window, CYAN_BLUE, self.player.hit_rect, 1)
            # pygame.draw.circle(self.window, CYAN_BLUE, self.red_ghost.rect.center, AVOID_RADIUS, 1)

        if self.paused:
            self.window.blit(self.dim_window, (0, 0))
            draw_text(self.window, "PAUSED", self.font_name, 100, WHITE, WIDTH / 2, HEIGHT / 2, "center")
        pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pygame.K_p:
                    self.paused = not self.paused

    def show_start_screen(self, status="start"):
        self.window.fill(WHITE)
        draw_text(self.window, "PacMan!", self.font_name, 100, DARKGREY, WIDTH / 2, HEIGHT / 2, "center")
        if status == "again":
            draw_text(self.window, "Press a key to start", self.font_name, 20, BLACK, WIDTH / 2, HEIGHT - 50, "center")
        else:
            draw_text(self.window, "Press a key twice to start", self.font_name, 20, BLACK, WIDTH / 2, HEIGHT - 50, "center")

        pygame.display.flip()
        self.wait_for_key()

    def show_win_screen(self):
        self.window.blit(self.dim_window, (0, 0))
        draw_text(self.window, "YOU WIN", self.font_name, 100, WHITE, WIDTH / 2, HEIGHT / 2 - 100, "center")
        draw_text(self.window, f"Your score:{self.score}", self.font_name, 80, WHITE, WIDTH / 2, HEIGHT / 2 , "center")
        draw_text(self.window, "Press a key to start again", self.font_name, 20, WHITE, WIDTH / 2, HEIGHT - 50, "center")

        pygame.display.flip()
        self.wait_for_key()
        self.show_start_screen("again")


    def show_go_screen(self):
        self.window.blit(self.dim_window, (0, 0))
        draw_text(self.window, "GAME OVER", self.font_name, 100, WHITE, WIDTH / 2, HEIGHT / 2, "center")
        draw_text(self.window, "Press a key to start", self.font_name, 20, WHITE, WIDTH / 2, HEIGHT - 50, "center")

        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pygame.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pygame.KEYUP:
                    waiting = False
