import sys

import pygame.event

from .Obstacle import Obstacle
from .TiledMap import TiledMap
from .draw_text import draw_text
from .setting import *
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
        for i in range(1, 2):
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
        self.small_dot_img = pygame.image.load(path.join(img_dir, "dot.png")).convert_alpha()
        self.big_dot_img = pygame.image.load(path.join(img_dir, "point.png")).convert_alpha()
        self.small_dot_img = pygame.transform.scale(self.small_dot_img, (8, 8))
        self.big_dot_img = pygame.transform.scale(self.big_dot_img, (20, 20))
        """blue ghost"""
        self.blue_ghost_d = pygame.image.load(path.join(img_dir, BLUE_GHOST_IMG)).convert_alpha()
        self.blue_ghost_u = pygame.image.load(path.join(img_dir, BLUE_GHOST_IMG_U)).convert_alpha()
        self.blue_ghost_r = pygame.image.load(path.join(img_dir, BLUE_GHOST_IMG_R)).convert_alpha()
        self.blue_ghost_l = pygame.image.load(path.join(img_dir, BLUE_GHOST_IMG_L)).convert_alpha()
        self.blue_ghost_d = pygame.transform.scale(self.blue_ghost_d, (TILE_SIZE, TILE_SIZE))
        self.blue_ghost_u = pygame.transform.scale(self.blue_ghost_u, (TILE_SIZE, TILE_SIZE))
        self.blue_ghost_r = pygame.transform.scale(self.blue_ghost_r, (TILE_SIZE, TILE_SIZE))
        self.blue_ghost_l = pygame.transform.scale(self.blue_ghost_l, (TILE_SIZE, TILE_SIZE))
        """green ghost"""
        self.green_ghost_d = pygame.image.load(path.join(img_dir, GREEN_GHOST_IMG)).convert_alpha()
        self.green_ghost_u = pygame.image.load(path.join(img_dir, GREEN_GHOST_IMG_U)).convert_alpha()
        self.green_ghost_r = pygame.image.load(path.join(img_dir, GREEN_GHOST_IMG_R)).convert_alpha()
        self.green_ghost_l = pygame.image.load(path.join(img_dir, GREEN_GHOST_IMG_L)).convert_alpha()
        self.green_ghost_d = pygame.transform.scale(self.green_ghost_d, (TILE_SIZE, TILE_SIZE))
        self.green_ghost_u = pygame.transform.scale(self.green_ghost_u, (TILE_SIZE, TILE_SIZE))
        self.green_ghost_r = pygame.transform.scale(self.green_ghost_r, (TILE_SIZE, TILE_SIZE))
        self.green_ghost_l = pygame.transform.scale(self.green_ghost_l, (TILE_SIZE, TILE_SIZE))
        """red ghost"""
        self.red_ghost_d = pygame.image.load(path.join(img_dir, RED_GHOST_IMG)).convert_alpha()
        self.red_ghost_u = pygame.image.load(path.join(img_dir, RED_GHOST_IMG_U)).convert_alpha()
        self.red_ghost_r = pygame.image.load(path.join(img_dir, RED_GHOST_IMG_R)).convert_alpha()
        self.red_ghost_l = pygame.image.load(path.join(img_dir, RED_GHOST_IMG_L)).convert_alpha()
        self.red_ghost_d = pygame.transform.scale(self.red_ghost_d, (TILE_SIZE, TILE_SIZE))
        self.red_ghost_u = pygame.transform.scale(self.red_ghost_u, (TILE_SIZE, TILE_SIZE))
        self.red_ghost_r = pygame.transform.scale(self.red_ghost_r, (TILE_SIZE, TILE_SIZE))
        self.red_ghost_l = pygame.transform.scale(self.red_ghost_l, (TILE_SIZE, TILE_SIZE))
        """pink ghost"""
        self.pink_ghost_d = pygame.image.load(path.join(img_dir, PINK_GHOST_IMG)).convert_alpha()
        self.pink_ghost_u = pygame.image.load(path.join(img_dir, PINK_GHOST_IMG_U)).convert_alpha()
        self.pink_ghost_r = pygame.image.load(path.join(img_dir, PINK_GHOST_IMG_R)).convert_alpha()
        self.pink_ghost_l = pygame.image.load(path.join(img_dir, PINK_GHOST_IMG_L)).convert_alpha()
        self.pink_ghost_d = pygame.transform.scale(self.pink_ghost_d, (TILE_SIZE, TILE_SIZE))
        self.pink_ghost_u = pygame.transform.scale(self.pink_ghost_u, (TILE_SIZE, TILE_SIZE))
        self.pink_ghost_r = pygame.transform.scale(self.pink_ghost_r, (TILE_SIZE, TILE_SIZE))
        self.pink_ghost_l = pygame.transform.scale(self.pink_ghost_l, (TILE_SIZE, TILE_SIZE))
        """orange ghost"""
        self.orange_ghost_d = pygame.image.load(path.join(img_dir, ORANGE_GHOST_IMG)).convert_alpha()
        self.orange_ghost_u = pygame.image.load(path.join(img_dir, ORANGE_GHOST_IMG_U)).convert_alpha()
        self.orange_ghost_r = pygame.image.load(path.join(img_dir, ORANGE_GHOST_IMG_R)).convert_alpha()
        self.orange_ghost_l = pygame.image.load(path.join(img_dir, ORANGE_GHOST_IMG_L)).convert_alpha()
        self.orange_ghost_d = pygame.transform.scale(self.orange_ghost_d, (TILE_SIZE, TILE_SIZE))
        self.orange_ghost_u = pygame.transform.scale(self.orange_ghost_u, (TILE_SIZE, TILE_SIZE))
        self.orange_ghost_r = pygame.transform.scale(self.orange_ghost_r, (TILE_SIZE, TILE_SIZE))
        self.orange_ghost_l = pygame.transform.scale(self.orange_ghost_l, (TILE_SIZE, TILE_SIZE))

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
        #
        Point(self, 30, 30)
        #
        Point(self, WIDTH - 30, 30)
        #
        Point(self, 30, HEIGHT - 30)
        #
        Point(self, WIDTH - 30, HEIGHT - 30)
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
        self.draw_debug = False
        self.paused = False


    def run(self):
        # game loop - set self.playing = False to end the game
        self.runing = True
        while self.runing:
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
        hits = pygame.sprite.spritecollide(self.player, self.ghosts, False)
        for hit in hits:
            self.runing = False

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
        if len(self.dots) is 0:
            self.window.fill(CYAN_BLUE)
        draw_text(self, self.window, str(self.score),30, WHITE,  WIDTH / 2, 10, "n")
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
            pygame.draw.circle(self.window, CYAN_BLUE, self.red_ghost.rect.center, AVOID_RADIUS, 1)

        if self.paused:
            self.window.blit(self.dim_window, (0, 0))
            draw_text(self, self.window, "PAUSED", 100, WHITE, WIDTH / 2, HEIGHT / 2, "center")
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

    def show_start_screen(self):
        pass

    def show_go_screen(self):
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
