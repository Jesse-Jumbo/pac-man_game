import math
import sys

import pygame.event

from .Node import Node
from .Obstacle import Obstacle
from .TiledMap import TiledMap
from .collide_hit_rect import collide_hit_rect
from .collide_sprite_with_walls import collide_with_walls
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
from .SquareGrid import *


class Game:
    def __init__(self):
        # pygame base setting
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        # initialize all variables and so all the setup for a new game
        # control variables
        self.draw_debug = False
        self.check_path = False
        self.paused = False
        self.waiting = False
        self.danger = False
        self.stop_music = False
        self.blue_ghost = False
        # load all img and music data from folder
        self.player_images = []
        self.ghosts_images = {BLUE_IMG: {}, RED_IMG: {}, PINK_IMG: {}, GREEN_IMG: {}, ORANGE_IMG: {}}
        self.load_data()
        # initialize sprites group
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.nodes = pygame.sprite.Group()
        # create map object
        self.map.make_map(self, WALL_LAYER_NAME)
        self.map.make_map(self, DOTS_LAYER_NAME)
        self.map.make_map(self, POINT_LAYER_NAME)
        self.player = self.map.make_map(self, PLAYER_LAYER_NAME)
        self.red_ghost = self.map.make_map(self, RED_GHOST_LAYER_NAME)
        self.pink_ghost = self.map.make_map(self, PINK_GHOST_LAYER_NAME)
        self.green_ghost = self.map.make_map(self, GREEN_GHOST_LAYER_NAME)
        self.orange_ghost = self.map.make_map(self, ORANGE_GHOST_LAYER_NAME)
        # create nodes
        self.node_pos = []
        temp_pos = []
        wall_pos = []
        for wall in self.walls:
            wall_pos.append(vec(wall.pos))
        for x in range(0, WIDTH, TILE_SIZE):
            for y in range(0, HEIGHT, TILE_SIZE):
                temp_pos.append(vec(x, y))
        for node in temp_pos:
            if node not in wall_pos:
                n = Node(node[0], node[1])
                self.nodes.add(n)
                self.node_pos.append(node)

    def load_data(self):
        """folder path"""
        game_dir = path.dirname(__file__)
        img_dir = path.join(game_dir, '../img')
        self.snd_dir = path.join(game_dir, '../snd')
        map_dir = path.join(game_dir, '../maps')
        '''font'''
        self.font_name = pygame.font.match_font('arial')
        '''pause view'''
        self.dim_window = pygame.Surface(self.window.get_size()).convert_alpha()
        self.dim_window.fill((0, 0, 0, 100))
        '''load map'''
        for i in range(5, 6):
            self.map = TiledMap(path.join(map_dir, f'map0{i}.tmx'))
        """img"""
        """player movement animation"""
        for i in ["cc", "c", "o", "oo"]:
            self.player_images.append(pygame.transform.scale(pygame.image.load(path.join(img_dir, f"pac_man_{i}.png")).convert_alpha(), (TILE_SIZE, TILE_SIZE)))
        """blue ghost"""
        for key, value, in blue_ghost_image_dic.items():
            self.ghosts_images[BLUE_IMG][key] = pygame.image.load(path.join(img_dir, value)).convert_alpha()
            image = self.ghosts_images[BLUE_IMG][key]
            self.ghosts_images[BLUE_IMG][key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        """red ghost"""
        for key, value, in red_ghost_image_dic.items():
            self.ghosts_images[RED_IMG][key] = pygame.image.load(path.join(img_dir, value)).convert_alpha()
            image = self.ghosts_images[RED_IMG][key]
            self.ghosts_images[RED_IMG][key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        """pink ghost"""
        for key, value, in pink_ghost_image_dic.items():
            self.ghosts_images[PINK_IMG][key] = pygame.image.load(path.join(img_dir, value)).convert_alpha()
            image = self.ghosts_images[PINK_IMG][key]
            self.ghosts_images[PINK_IMG][key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        """green ghost"""
        for key, value, in green_ghost_image_dic.items():
            self.ghosts_images[GREEN_IMG][key] = pygame.image.load(path.join(img_dir, value)).convert_alpha()
            image = self.ghosts_images[GREEN_IMG][key]
            self.ghosts_images[GREEN_IMG][key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        """orange ghost"""
        for key, value, in orange_ghost_image_dic.items():
            self.ghosts_images[ORANGE_IMG][key] = pygame.image.load(path.join(img_dir, value)).convert_alpha()
            image = self.ghosts_images[ORANGE_IMG][key]
            self.ghosts_images[ORANGE_IMG][key] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

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
            self.show_go_screen()
            self.__init__()

    def draw(self):
        # cover last update
        self.window.fill(BLACK)
        # check FPS is correctly
        pygame.display.set_caption(TITLE + "{:.2f}".format(self.clock.get_fps()))
        draw_text(self.window, str(self.player.score), self.font_name, 30, WHITE,  WIDTH / 2, 10, "n")
        # draw all sprites according to sprite's rect
        for sprite in self.all_sprites:
            self.window.blit(sprite.image, sprite.rect)
            # press H to check sprite rect
            if self.draw_debug:
                pygame.draw.rect(self.window, BG_COLOR, sprite.rect, 1)
                pygame.draw.rect(self.window, BG_COLOR, sprite.hit_rect, 1)

        if self.draw_debug:
            for node in self.nodes:
                pygame.draw.rect(self.window, RED, node.pos_rect, 1)
            for wall in self.walls:
                pygame.draw.rect(self.window, BG_COLOR, wall.hit_rect, 1)
        if self.draw_debug:
            for dot in self.dots:
                pygame.draw.rect(self.window, BG_COLOR, dot.hit_rect, 1)
        if self.draw_debug:
            for point in self.points:
                pygame.draw.rect(self.window, BG_COLOR, point.hit_rect, 1)
        # press P to pause game
        if self.paused:
            self.window.blit(self.dim_window, (0, 0))
            draw_text(self.window, "PAUSED", self.font_name, TITLE_SIZE, WHITE, WIDTH_CENTER, HEIGHT_CENTER, "center")
        # update game view
        pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    self.quit()
                if event.key == pygame.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                if event.key == pygame.K_ESCAPE:
                    self.stop_music = not self.stop_music
                # check ghost search path
                if event.key == pygame.K_r:
                    self.red_ghost.draw_check_path = not self.red_ghost.draw_check_path
                if event.key == pygame.K_k:
                    self.pink_ghost.draw_check_path = not self.pink_ghost.draw_check_path
                if event.key == pygame.K_o:
                    self.orange_ghost.draw_check_path = not self.orange_ghost.draw_check_path
                if event.key == pygame.K_g:
                    self.green_ghost.draw_check_path = not self.green_ghost.draw_check_path

                # for player
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_KP_8:
                    self.player.up_move = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_KP_2:
                    self.player.down_move = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_KP_4:
                    self.player.left_move = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_KP_6:
                    self.player.right_move = True
            if event.type == pygame.KEYUP:
                # for player
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_KP_8:
                    self.player.down_move = False
                    self.player.right_move = False
                    self.player.left_move = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_KP_2:
                    self.player.up_move = False
                    self.player.right_move = False
                    self.player.left_move = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_KP_4:
                    self.player.up_move = False
                    self.player.down_move = False
                    self.player.right_move = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_KP_6:
                    self.player.up_move = False
                    self.player.down_move = False
                    self.player.left_move = False


    def show_go_screen(self):
        self.window.blit(self.dim_window, (0, 0))
        draw_text(self.window, f"SCORE: {self.player.score}", self.font_name, TITLE_SIZE, WHITE, WIDTH_CENTER, HEIGHT_CENTER, "center")
        draw_text(self.window, "Press a key to start", self.font_name, 20, WHITE, WIDTH_CENTER, HEIGHT - 50, "center")

        pygame.display.flip()
        self.wait_for_key()
        self.__init__()

    def wait_for_key(self):
        self.music_play()
        pygame.event.wait()
        self.waiting = True
        self.music_play()
        while self.waiting:
            self.danger = False
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.quit()
                if event.type == pygame.KEYUP:
                    pygame.mixer.music.stop()
                    self.waiting = False
        self.music_play()

    def music_play(self):
        if self.waiting or self.paused:
            pygame.mixer.music.load(path.join(self.snd_dir, MENU_SND))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(loops=-1)
        elif self.danger:
            pygame.mixer.music.load(path.join(self.snd_dir, ALL_GHOST_GO_OUT))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(loops=-1)
        elif self.stop_music:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.load(path.join(self.snd_dir, BGM))
            pygame.mixer.music.set_volume(0.8)
            pygame.mixer.music.play(loops=-1)
