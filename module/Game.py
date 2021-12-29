import sys

import pygame.event

from .setting import *
from .PacMan import PacMan
from .Dot import Dot
from .Point import Point
from .RedGhost import RedGhost
from .GreenGhost import GreenGhost
from .PinkGhost import PinkGhost
from .OrangeGhost import OrangeGhost
from .draw_score import draw_score
from .Ghost import Ghost


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        # pygame.key.set_repeat(500, 100)
        self.load_data()

        self.score = 0

    def load_data(self):
        """folder path"""
        game_dir = path.dirname(__file__)
        img_dir = path.join(game_dir, '../img')
        snd_dir = path.join(game_dir, '../snd')
        '''font'''
        self.font_name = pygame.font.match_font('arial')

        """img"""
        """player"""
        self.player_img = pygame.image.load(path.join(img_dir, "pac.png")).convert_alpha()
        self.player_img = pygame.transform.scale(self.player_img, (20, 20))
        self.up_img = pygame.transform.scale((pygame.transform.rotate(self.player_img, 90)), (20, 20))
        self.down_img = pygame.transform.scale((pygame.transform.rotate(self.player_img, 270)), (20, 20))
        self.turn_left_image = pygame.transform.scale((pygame.transform.flip(self.player_img, True, False)), (20, 20))
        """dot"""
        self.small_dot_img = pygame.image.load(path.join(img_dir, "dot.png")).convert_alpha()
        self.big_dot_img = pygame.image.load(path.join(img_dir, "point.png")).convert_alpha()
        self.small_dot_img = pygame.transform.scale(self.small_dot_img, (8, 8))
        self.big_dot_img = pygame.transform.scale(self.big_dot_img, (20, 20))
        """blue ghost"""
        self.blue_ghost_d = pygame.image.load(path.join(img_dir, "blue_ghost_d.png")).convert_alpha()
        self.blue_ghost_u = pygame.image.load(path.join(img_dir, "blue_ghost_u.png")).convert_alpha()
        self.blue_ghost_r = pygame.image.load(path.join(img_dir, "blue_ghost_r.png")).convert_alpha()
        self.blue_ghost_l = pygame.image.load(path.join(img_dir, "blue_ghost_l.png")).convert_alpha()
        self.blue_ghost_d = pygame.transform.scale(self.blue_ghost_d, (20, 25))
        self.blue_ghost_u = pygame.transform.scale(self.blue_ghost_u, (20, 25))
        self.blue_ghost_r = pygame.transform.scale(self.blue_ghost_r, (20, 25))
        self.blue_ghost_l = pygame.transform.scale(self.blue_ghost_l, (20, 25))
        """green ghost"""
        self.green_ghost_d = pygame.image.load(path.join(img_dir, "green_ghost_d.png")).convert_alpha()
        self.green_ghost_u = pygame.image.load(path.join(img_dir, "green_ghost_u.png")).convert_alpha()
        self.green_ghost_r = pygame.image.load(path.join(img_dir, "green_ghost_r.png")).convert_alpha()
        self.green_ghost_l = pygame.image.load(path.join(img_dir, "green_ghost_l.png")).convert_alpha()
        self.green_ghost_d = pygame.transform.scale(self.green_ghost_d, (20, 25))
        self.green_ghost_u = pygame.transform.scale(self.green_ghost_u, (20, 25))
        self.green_ghost_r = pygame.transform.scale(self.green_ghost_r, (20, 25))
        self.green_ghost_l = pygame.transform.scale(self.green_ghost_l, (20, 25))
        """red ghost"""
        self.red_ghost_d = pygame.image.load(path.join(img_dir, "red_ghost_d.png")).convert_alpha()
        self.red_ghost_u = pygame.image.load(path.join(img_dir, "red_ghost_u.png")).convert_alpha()
        self.red_ghost_r = pygame.image.load(path.join(img_dir, "red_ghost_r.png")).convert_alpha()
        self.red_ghost_l = pygame.image.load(path.join(img_dir, "red_ghost_l.png")).convert_alpha()
        self.red_ghost_d = pygame.transform.scale(self.red_ghost_d, (20, 25))
        self.red_ghost_u = pygame.transform.scale(self.red_ghost_u, (20, 25))
        self.red_ghost_r = pygame.transform.scale(self.red_ghost_r, (20, 25))
        self.red_ghost_l = pygame.transform.scale(self.red_ghost_l, (20, 25))
        """pink ghost"""
        self.pink_ghost_u = pygame.image.load(path.join(img_dir, "pink_ghost_u.png")).convert_alpha()
        self.pink_ghost_d = pygame.image.load(path.join(img_dir, "pink_ghost_d.png")).convert_alpha()
        self.pink_ghost_r = pygame.image.load(path.join(img_dir, "pink_ghost_r.png")).convert_alpha()
        self.pink_ghost_l = pygame.image.load(path.join(img_dir, "pink_ghost_l.png")).convert_alpha()
        self.pink_ghost_d = pygame.transform.scale(self.pink_ghost_d, (20, 25))
        self.pink_ghost_u = pygame.transform.scale(self.pink_ghost_u, (20, 25))
        self.pink_ghost_r = pygame.transform.scale(self.pink_ghost_r, (20, 25))
        self.pink_ghost_l = pygame.transform.scale(self.pink_ghost_l, (20, 25))
        """orange ghost"""
        self.orange_ghost_u = pygame.image.load(path.join(img_dir, "orange_ghost_u.png")).convert_alpha()
        self.orange_ghost_d = pygame.image.load(path.join(img_dir, "orange_ghost_d.png")).convert_alpha()
        self.orange_ghost_r = pygame.image.load(path.join(img_dir, "orange_ghost_r.png")).convert_alpha()
        self.orange_ghost_l = pygame.image.load(path.join(img_dir, "orange_ghost_l.png")).convert_alpha()
        self.orange_ghost_d = pygame.transform.scale(self.orange_ghost_d, (20, 25))
        self.orange_ghost_u = pygame.transform.scale(self.orange_ghost_u, (20, 25))
        self.orange_ghost_r = pygame.transform.scale(self.orange_ghost_r, (20, 25))
        self.orange_ghost_l = pygame.transform.scale(self.orange_ghost_l, (20, 25))

    def new(self):
        # initialize all variables and so all the setup for a new game
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.player = PacMan(self, WIDTH / 2, HEIGHT - 50)
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
        #
        RedGhost(self, WIDTH/2, HEIGHT/2-17.5)
        #
        GreenGhost(self, WIDTH/2-20, HEIGHT/2+8)
        #
        PinkGhost(self, WIDTH/2, HEIGHT/2+8)
        #
        OrangeGhost(self, WIDTH/2+20, HEIGHT/2+8)


    def run(self):
        # game loop - set self.playing = False to end the game
        self.runing = True
        while self.runing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
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
        self.window.fill(BLACK)
        self.draw_grid()
        if len(self.dots) is 0:
            self.window.fill(CYAN_BLUE)
        self.score_draw = draw_score(self, self.window, str(self.score), 30, WIDTH / 2, 10)
        self.all_sprites.draw(self.window)
        pygame.display.flip()

    def events(self):
        # catch all events here
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                self.quit()

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
