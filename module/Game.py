import sys

import pygame.event

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
from .Node import *


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
        self.paused = False
        self.waiting = False
        self.danger = False
        self.stop_music = False
        # load all img and music data from folder
        self.player_images = {RIGHT_IMG: [], DOWN_IMG: [], LEFT_IMG: [], UP_IMG: []}
        self.ghosts_images = {BLUE_IMG: {}, RED_IMG: {}, PINK_IMG: {}, GREEN_IMG: {}, ORANGE_IMG: {}}
        self.load_data()
        # initialize sprites group
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.Group()
        self.nodes = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        # create map object
        self.map.make_map(self, WALL_LAYER_NAME)
        self.map.make_map(self, POINT_LAYER_NAME)
        self.red_ghost = self.map.make_map(self, RED_GHOST_LAYER_NAME)
        self.pink_ghost = self.map.make_map(self, PINK_GHOST_LAYER_NAME)
        self.green_ghost = self.map.make_map(self, GREEN_GHOST_LAYER_NAME)
        self.orange_ghost = self.map.make_map(self, ORANGE_GHOST_LAYER_NAME)
        self.player = self.map.make_map(self, PLAYER_LAYER_NAME)
        self.map.make_map(self, DOTS_LAYER_NAME)
        # track time variables
        self.blue_time = pygame.time.get_ticks()

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
        # """wall"""
        # self.wall_img = pygame.image.load(path.join(img_dir, WALL_IMG)).convert_alpha()
        # self.wall_img = pygame.transform.scale(self.wall_img, (TILE_SIZE, TILE_SIZE))
        """player movement animation"""
        for i in ["cc", "c", "o", "oo"]:
            self.player_images[RIGHT_IMG].append(pygame.transform.scale(pygame.image.load(path.join(img_dir, f"pac_man_{i}.png")).convert_alpha(), (TILE_SIZE, TILE_SIZE)))
        for player_img in self.player_images[RIGHT_IMG]:
            self.player_images[UP_IMG].append(
                pygame.transform.scale((pygame.transform.rotate(player_img, 90)), (TILE_SIZE, TILE_SIZE)))
            self.player_images[DOWN_IMG].append(
                pygame.transform.scale((pygame.transform.rotate(player_img, 270)), (TILE_SIZE, TILE_SIZE)))
            self.player_images[LEFT_IMG].append(
                pygame.transform.scale((pygame.transform.flip(player_img, True, False)), (TILE_SIZE, TILE_SIZE)))
        # """dot and point"""
        # self.small_dot_img = pygame.image.load(path.join(img_dir, DOT_IMG)).convert_alpha()
        # self.big_dot_img = pygame.image.load(path.join(img_dir, POINT_IMG)).convert_alpha()
        # self.small_dot_img = pygame.transform.scale(self.small_dot_img, (8, 8))
        # self.big_dot_img = pygame.transform.scale(self.big_dot_img, (20, 20))
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

        hits = pygame.sprite.spritecollide(self.player, self.points, True, collide_hit_rect)
        for hit in hits:
            self.player.score += 50
            self.red_ghost.blue_time()
            self.green_ghost.blue_time()
            self.pink_ghost.blue_time()
            self.orange_ghost.blue_time()
            self.danger = True
            self.music_play()

    def draw_grid(self):
        # check the background is drawn correctly with the tile size
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.window, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.window, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # cover last update
        self.window.fill(BG_COLOR)
        # check FPS is correctly
        pygame.display.set_caption(TITLE + "{:.2f}".format(self.clock.get_fps()))
        draw_text(self.window, str(self.player.score), self.font_name, 30, WHITE,  WIDTH / 2, 10, "n")
        # self.draw_grid()
        # draw all sprites according to sprite's rect
        for sprite in self.all_sprites:
            self.window.blit(sprite.image, sprite.rect)
            # press H to check sprite rect
            if self.draw_debug:
                pygame.draw.rect(self.window, CYAN_BLUE, sprite.rect, 1)
                pygame.draw.rect(self.window, CYAN_BLUE, sprite.hit_rect, 1)
        if self.draw_debug:
            for wall in self.walls:
                pygame.draw.rect(self.window, CYAN_BLUE, wall.hit_rect, 1)
        # TODO check hit rect by draw
        if self.draw_debug:
            for dot in self.dots:
                pygame.draw.rect(self.window, CYAN_BLUE, dot.hit_rect, 1)
        if self.draw_debug:
            for point in self.points:
                pygame.draw.rect(self.window, CYAN_BLUE, point.hit_rect, 1)
        # press P to pause game
        if self.paused:
            self.window.blit(self.dim_window, (0, 0))
            draw_text(self.window, "PAUSED", self.font_name, 100, WHITE, WIDTH / 2, HEIGHT / 2, "center")
        # update game view
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
                if event.key == pygame.K_ESCAPE:
                    self.stop_music = not self.stop_music
                # for player
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.up_move = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.down_move = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.left_move = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.right_move = True
            if event.type == pygame.KEYUP:
                # for player
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.down_move = False
                    self.player.right_move = False
                    self.player.left_move = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.up_move = False
                    self.player.right_move = False
                    self.player.left_move = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.up_move = False
                    self.player.down_move = False
                    self.player.right_move = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.up_move = False
                    self.player.down_move = False
                    self.player.left_move = False


    def show_go_screen(self):
        self.window.blit(self.dim_window, (0, 0))
        draw_text(self.window, f"SCORE: {self.player.score}", self.font_name, 100, WHITE, WIDTH / 2, HEIGHT / 2, "center")
        draw_text(self.window, "Press a key to start", self.font_name, 20, WHITE, WIDTH / 2, HEIGHT - 50, "center")

        pygame.display.flip()
        self.wait_for_key()

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
