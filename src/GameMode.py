import random
import sys

import pygame.event

from games.pac_man.src.Node import Node
from games.pac_man.src.TiledMap import TiledMap
from games.pac_man.module.draw_text import draw_text
from games.pac_man.src.SquareGrid import *
from mlgame.gamedev.game_interface import GameResultState
from .collide_hit_rect import collide_with_walls, collide_player_with_ghosts, collide_with_nodes
from games.pac_man.src.collide_hit_rect import collide_hit_rect

from .env import *


class GameMode:
    def __init__(self):
        # initialize all variables and so all the setup for a new game
        # TODO reset where initialize
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        # control variables
        self.playing = True
        self.draw_debug = False
        self.check_path = False
        self.paused = False
        self.waiting = False
        self.danger = False
        self.stop_music = False
        self.blue_ghost = False
        # load all img and music data from folder
        self.load_data()
        # initialize sprites group
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.nodes = pygame.sprite.Group()
        # create map object
        self.map.make_map(WALL_LAYER_NAME)
        self.map.make_map(DOTS_LAYER_NAME)
        self.map.make_map(POINT_LAYER_NAME)
        self.player = self.map.make_map(PLAYER_LAYER_NAME)
        self.red_ghost = self.map.make_map(RED_GHOST_LAYER_NAME)
        self.pink_ghost = self.map.make_map(PINK_GHOST_LAYER_NAME)
        self.green_ghost = self.map.make_map(GREEN_GHOST_LAYER_NAME)
        self.orange_ghost = self.map.make_map(ORANGE_GHOST_LAYER_NAME)
        # TODO refactor load tiled map mean
        # self.map.make_map()
        # add sprite group
        for wall in self.map.walls:
            self.all_sprites.add(wall)
            self.walls.add(wall)
        for point in self.map.points:
            self.all_sprites.add(point)
            self.points.add(point)
        for dot in self.map.dots:
            self.all_sprites.add(dot)
            self.dots.add(dot)
        self.all_sprites.add(self.player)
        self.ghosts.add(self.red_ghost)
        self.ghosts.add(self.pink_ghost)
        self.ghosts.add(self.green_ghost)
        self.ghosts.add(self.orange_ghost)

        # create nodes
        self.node_pos = []
        temp_pos = []
        wall_pos = []
        for wall in self.walls:
            wall_pos.append(vec(wall.pos))
        for x in range(0, WIDTH, TILE_X_SIZE):
            for y in range(0, HEIGHT, TILE_X_SIZE):
                temp_pos.append(vec(x, y))
        for node in temp_pos:
            if node not in wall_pos:
                n = Node(node[0], node[1])
                self.nodes.add(n)
                self.node_pos.append(node)
        # game variables
        self.frame = 0
        '''state include GameResultState.FINISH、GameResultState.FAIL"'''
        self.state = GameResultState.FAIL

    def load_data(self):
        '''font'''
        # self.font_name = pygame.font.match_font('arial')
        '''pause view'''
        # self.dim_window = pygame.Surface(self.window.get_size()).convert_alpha()
        # self.dim_window.fill((0, 0, 0, 100))
        '''load map'''
        self.map = TiledMap(path.join(MAP_DIR, MAP_NAME))

    def judge_ghost_could_out(self):
        if len(self.dots) < len(self.dots) + RED_GO:
            self.red_ghost.is_out = True
        if len(self.dots) < len(self.dots) + PINK_GO:
            self.pink_ghost.is_out = True
        if len(self.dots) < len(self.dots) + GREEN_GO:
            self.green_ghost.is_out = True
        if len(self.dots) < len(self.dots) + ORANGE_GO:
            self.orange_ghost.is_out = True

    def get_result(self) -> list:
        res = [{"player": f"{self.player.player_no}P",
                "score": self.player.score,
                "used_frame": self.frame}]
        return res

    def run(self, commands):
        # game loop - set self.playing = False to end the game
        # while self.playing:
        self.events(commands)
        if not self.paused:
            self.update()
        self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def get_move_path(self, ghost_no: str):
        if ghost_no not in GHOST_NO_LIST:
            print("ghost number false")
        else:
            # TODO reduce hierarchy
            # red ghost goal is player
            if ghost_no == RED_GHOST_NO:
                if self.red_ghost.is_blue:
                    return self.red_ghost.frightened_module(self.walls)
                else:
                    return self.red_ghost.chase_module(self.walls, self.player.node_pos)
            # pink ghost goal is player front
            if ghost_no == PINK_GHOST_NO:
                if self.pink_ghost.is_blue:
                    return self.pink_ghost.frightened_module(self.walls)
                else:
                    return self.pink_ghost.chase_module(self.walls, self.player.front_node_pos)
            # green ghost goal random choice all object
            if ghost_no == GREEN_GHOST_NO:
                if self.green_ghost.is_blue:
                    return self.green_ghost.frightened_module(self.walls)
                else:
                    goal = []
                    for ghost in self.ghosts:
                        goal.append(ghost.node_pos)
                    goal.append(self.player.node_pos)
                    goal.append(self.player.front_node_pos)
                    return self.green_ghost.chase_module(self.walls, random.choice(goal))
            # orange ghost goal random choice all node
            if ghost_no == ORANGE_GHOST_NO:
                if self.orange_ghost.is_blue:
                    self.orange_ghost.frightened_module(self.walls)
                else:
                    node_pos = pygame.math.Vector2(random.choice(list(self.node_pos)))
                    return self.orange_ghost.chase_module(self.walls, vec(node_pos / TILE_X_SIZE))

    def update_ghost(self):
        self.judge_ghost_could_out()

        self.red_ghost.update(self.get_move_path(RED_GHOST_NO))
        self.pink_ghost.update(self.get_move_path(PINK_GHOST_NO))
        self.green_ghost.update(self.get_move_path(GREEN_GHOST_NO))
        self.orange_ghost.update(self.get_move_path(ORANGE_GHOST_NO))

    def update(self):
        self.frame += 1
        # update potion of the game loop
        self.all_sprites.update()
        self.update_ghost()
        # game over?
        if len(self.dots) == 0 and self.player.score != 0:
            self.playing = False
            self.__init__()

    def draw(self):
        pass
        # TODO refactor game draw
        # # check FPS is correctly
        # draw_text(self.window, str(self.player.score), self.font_name, 30, WHITE,  WIDTH / 2, 10, "n")
        # # draw all sprites according to sprite's rect
        # for sprite in self.all_sprites:
        #     self.window.blit(sprite.image, sprite.rect)
        #     # press H to check sprite rect
        #     if self.draw_debug:
        #         pygame.draw.rect(self.window, BG_COLOR, sprite.rect, 1)
        #         pygame.draw.rect(self.window, BG_COLOR, sprite.hit_rect, 1)
        #
        # if self.draw_debug:
        #     for node in self.nodes:
        #         pygame.draw.rect(self.window, RED, node.pos_rect, 1)
        #     for wall in self.walls:
        #         pygame.draw.rect(self.window, BG_COLOR, wall.hit_rect, 1)
        # if self.draw_debug:
        #     for dot in self.dots:
        #         pygame.draw.rect(self.window, BG_COLOR, dot.hit_rect, 1)
        # if self.draw_debug:
        #     for point in self.points:
        #         pygame.draw.rect(self.window, BG_COLOR, point.hit_rect, 1)
        # # press P to pause game
        # if self.paused:
        #     self.window.blit(self.dim_window, (0, 0))
        #     draw_text(self.window, "PAUSED", self.font_name, TITLE_SIZE, WHITE, WIDTH_CENTER, HEIGHT_CENTER, "center")
        # # update game view
        # pygame.display.flip()

    def events(self, commands):
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

        # print(commands)
                # for player
                # if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_KP_8:
                #     self.player.up_move = True
            #     if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_KP_2:
            #         self.player.down_move = True
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_KP_4:
            #         self.player.left_move = True
            #     if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_KP_6:
            #         self.player.right_move = True
            # if event.type == pygame.KEYUP:
                # for player
                # if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_KP_8:
                #     self.player.down_move = False
                #     self.player.right_move = False
                #     self.player.left_move = False
            #     if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_KP_2:
            #         self.player.up_move = False
            #         self.player.right_move = False
            #         self.player.left_move = False
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_KP_4:
            #         self.player.up_move = False
            #         self.player.down_move = False
            #         self.player.right_move = False
            #     if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_KP_6:
            #         self.player.up_move = False
            #         self.player.down_move = False
            #         self.player.left_move = False

    def check_collisions(self):
        # for player
        collide_with_walls(self.player, self.walls, 'x')
        collide_with_walls(self.player, self.walls, 'y')
        collide_player_with_ghosts(self.player, self.ghosts)
        collide_with_nodes(self.player, self.nodes)

        hits = pygame.sprite.spritecollide(self.player, self.dots, True, collide_hit_rect)
        for hit in hits:
            self.player.score += DOT_SCORE
            self.player.speed += -0.001

        hits = pygame.sprite.spritecollide(self.player, self.points, True, collide_hit_rect)
        for hit in hits:
            self.player.score += POINT_SCORE
            self.player.score += POINT_SCORE
            self.red_ghost.blue_time()
            self.pink_ghost.blue_time()
            self.green_ghost.blue_time()
            self.orange_ghost.blue_time()
            self.danger = True
            self.play_music()

        # for ghost
        for ghost in self.ghosts:
            collide_with_walls(ghost, self.walls, 'x')
            collide_with_walls(ghost, self.walls, 'y')
            collide_with_nodes(ghost, self.nodes, dir="ghost")


    def show_go_screen(self):
        pass
        # TODO rethink need pause view
        # self.window.blit(self.dim_window, (0, 0))
        # draw_text(self.window, f"SCORE: {self.player.score}", self.font_name, TITLE_SIZE, WHITE, WIDTH_CENTER, HEIGHT_CENTER, "center")
        # draw_text(self.window, "Press a key to start", self.font_name, 20, WHITE, WIDTH_CENTER, HEIGHT - 50, "center")
        #
        # pygame.display.flip()
        # self.wait_for_key()

    def wait_for_key(self):
        pass
        # TODO rethink need the method
        # self.play_music()
        # pygame.event.wait()
        # self.waiting = True
        # self.play_music()
        # while self.waiting:
        #     self.danger = False
        #     self.clock.tick(FPS)
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             self.waiting = False
        #             self.quit()
        #         if event.type == pygame.KEYUP:
        #             pygame.mixer.music.stop()
        #             self.waiting = False
        # self.play_music()

    def play_music(self):
        pass
        # TODO reset where play music
        # if self.waiting or self.paused:
        #     pygame.mixer.music.load(path.join(self.snd_dir, MENU_SND))
        #     pygame.mixer.music.set_volume(0.2)
        #     pygame.mixer.music.play(loops=-1)
        # elif self.danger:
        #     pygame.mixer.music.load(path.join(self.snd_dir, ALL_GHOST_GO_OUT))
        #     pygame.mixer.music.set_volume(0.2)
        #     pygame.mixer.music.play(loops=-1)
        # elif self.stop_music:
        #     pygame.mixer.music.stop()
        # else:
        #     pygame.mixer.music.load(path.join(self.snd_dir, BGM))
        #     pygame.mixer.music.set_volume(0.8)
        #     pygame.mixer.music.play(loops=-1)
