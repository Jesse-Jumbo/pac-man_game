import random
import sys

import pygame.event

from games.PacMan.src.Node import Node
from games.PacMan.src.PacManMap import PacManMap
from games.PacMan.module.draw_text import draw_text
from games.PacMan.src.SquareGrid import *
from mlgame.gamedev.game_interface import GameResultState, GameStatus
from .collide_hit_rect import *
from games.PacMan.src.collide_hit_rect import collide_hit_rect

from .env import *


class GameMode:
    # TODO class type? object? for SoundController
    def __init__(self, map_name: str, time_limit: int, sound_controller):
        # initialize all variables and so all the setup for a new game
        self.time_limit = time_limit
        self.sound_controller = sound_controller
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        # control variables
        self.playing = True
        self.draw_debug = False
        self.check_path = False
        self.is_paused = False
        self.is_blue_ghost = False
        self.is_danger = False
        self.is_warn = False
        self.stop_music = False
        self.is_music_change = False
        # load all img and music data from folder
        self.map_name = map_name
        self.load_data()
        # initialize sprites group
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.power_pellets = pygame.sprite.Group()
        self.nodes = pygame.sprite.Group()
        '''load map'''
        self.map = PacManMap(path.join(MAP_DIR, self.map_name))
        self.map.make_map()
        # create map object
        self.player = self.map.player
        self.red_ghost = self.map.red_ghost
        self.pink_ghost = self.map.pink_ghost
        self.green_ghost = self.map.green_ghost
        self.orange_ghost = self.map.orange_ghost
        # add sprite group
        for wall in self.map.walls:
            self.all_sprites.add(wall)
            self.walls.add(wall)
        for power_pellet in self.map.power_pellets:
            self.all_sprites.add(power_pellet)
            self.power_pellets.add(power_pellet)
        for dot in self.map.dots:
            self.all_sprites.add(dot)
            self.dots.add(dot)

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
        self.blue_frame = self.frame
        '''state include GameResultState.FINISH、GameResultState.FAIL"'''
        self.state = GameResultState.FAIL
        self.status = GameStatus.GAME_ALIVE
        self.ghost_go_out_limit = len(self.dots)
        self.change_music("normal")

    def load_data(self):
        '''font'''
        # self.font_name = pygame.font.match_font('arial')
        '''pause view'''
        # self.dim_window = pygame.Surface(self.window.get_size()).convert_alpha()
        # self.dim_window.fill((0, 0, 0, 100))
        pass

    def judge_ghost_could_out(self):
        if self.frame == RED_GO_FRAME:
            self.red_ghost.is_out = True
            self.change_music("warn")
        if self.frame == PINK_GO_FRAME:
            self.pink_ghost.is_out = True
            self.change_music("warn")
        if self.frame == GREEN_GO_FRAME:
            self.green_ghost.is_out = True
            self.change_music("warn")
        if self.frame == ORANGE_GO_FRAME:
            self.orange_ghost.is_out = True
            self.change_music("warn")

    def get_result(self) -> list:
        res = [self.player.get_result()]
        return res

    def run(self, command: dict):
        self.events()
        if not self.is_paused:
            self.update(command)
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
                    return self.red_ghost.enter_frightened_mode(self.walls)
                else:
                    return self.red_ghost.enter_chase_mode(self.walls, self.player.node_pos)
            # pink ghost goal is player front
            if ghost_no == PINK_GHOST_NO:
                if self.pink_ghost.is_blue:
                    return self.pink_ghost.enter_frightened_mode(self.walls)
                else:
                    return self.pink_ghost.enter_chase_mode(self.walls, self.player.front_node_pos)
            # green ghost goal random choice all object
            if ghost_no == GREEN_GHOST_NO:
                if self.green_ghost.is_blue:
                    return self.green_ghost.enter_frightened_mode(self.walls)
                else:
                    goal = []
                    for ghost in self.ghosts:
                        goal.append(ghost.node_pos)
                    goal.append(self.player.node_pos)
                    goal.append(self.player.front_node_pos)
                    return self.green_ghost.enter_chase_mode(self.walls, random.choice(goal))
            # orange ghost goal random choice all node
            if ghost_no == ORANGE_GHOST_NO:
                if self.orange_ghost.is_blue:
                    self.orange_ghost.enter_frightened_mode(self.walls)
                else:
                    node_pos = pygame.math.Vector2(random.choice(list(self.node_pos)))
                    return self.orange_ghost.enter_chase_mode(self.walls, vec(node_pos / TILE_X_SIZE))

    def update_ghost(self):
        self.judge_ghost_could_out()
        self.ghosts.update([])
        # self.red_ghost.update(self.get_move_path(RED_GHOST_NO))
        # self.pink_ghost.update(self.get_move_path(PINK_GHOST_NO))
        # self.green_ghost.update(self.get_move_path(GREEN_GHOST_NO))
        # self.orange_ghost.update(self.get_move_path(ORANGE_GHOST_NO))

    def update(self, command: dict):
        self.status = GameStatus.GAME_ALIVE
        self.frame += 1
        # update potion of the game loop
        self.all_sprites.update()
        self.player.update(command)
        self.update_ghost()
        self.check_collisions()
        if len(self.dots) == 0 and self.player.score != 0:
            self.playing = False
            self.state = GameResultState.FINISH
            self.status = GameStatus.GAME_PASS
        if not self.player.state:
            self.state = GameResultState.FAIL
            self.status = GameStatus.GAME_OVER
            self.playing = False

        if self.is_music_change:
            self.play_music()

        if self.is_blue_ghost:
            if not self.red_ghost.is_blue and not self.pink_ghost.is_blue and not self.green_ghost.is_blue and not self.orange_ghost.is_blue:
                self.change_music("normal")
            if self.frame - self.blue_frame > 600:
                self.change_music("normal")

        if len(self.dots) == 4 and not self.is_danger:
            self.change_music("danger")

        if self.frame > self.time_limit:
            self.state = GameResultState.FAIL
            self.status = GameStatus.GAME_OVER


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
        #     for power_pellet in self.power_pellets:
        #         pygame.draw.rect(self.window, BG_COLOR, power_pellet.hit_rect, 1)
        # # press P to pause game
        # if self.is_paused:
        #     self.window.blit(self.dim_window, (0, 0))
        #     draw_text(self.window, "PAUSED", self.font_name, TITLE_SIZE, WHITE, WIDTH_CENTER, HEIGHT_CENTER, "center")
        # # update game view
        # pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_u:
                #     self.quit()
                if event.key == pygame.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pygame.K_p:
                    self.is_paused = not self.is_paused
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
        collide_with_walls(self.player, self.walls)
        collide_player_with_ghosts(self.player, self.ghosts)
        collide_with_dots(self.player, self.dots)
        collide_with_nodes(self.player, self.nodes)

        # TODO Don't know how to refactor
        hits = pygame.sprite.spritecollide(self.player, self.power_pellets, True, collide_hit_rect)
        for hit in hits:
            self.player.score += POWER_PELLET_SCORE
            self.player.power_pellets_score += POWER_PELLET_SCORE
            self.player.ate_power_pellets_times += 1
            self.red_ghost.get_blue_state()
            self.pink_ghost.get_blue_state()
            self.green_ghost.get_blue_state()
            self.orange_ghost.get_blue_state()
            self.blue_frame = self.frame
            self.change_music("blue")

        # for ghost
        for ghost in self.ghosts:
            collide_with_walls(ghost, self.walls)
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
        #     self.is_danger = False
        #     self.clock.tick(FPS)
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             self.waiting = False
        #             self.quit()
        #         if event.type == pygame.KEYUP:
        #             pygame.mixer.music.stop()
        #             self.waiting = False
        # self.play_music()

    def change_music(self, music_state="normal"):
        if music_state == "warn":
            self.is_warn = True
            self.is_music_change = True
        elif music_state == "danger":
            self.is_blue_ghost = False
            self.is_danger = True
            self.is_music_change = True
        elif music_state == "blue":
            self.is_blue_ghost = True
        else:
            self.is_blue_ghost = False
        if self.is_danger:
            return
        self.is_music_change = True

    def play_music(self):
        if self.is_warn:
            self.sound_controller.play_warn_sound()
            self.is_warn = False
        elif self.is_blue_ghost or self.is_paused:
            self.sound_controller.play_blue_music()
        elif self.is_danger:
            self.sound_controller.play_danger_music()
        else:
            self.sound_controller.play_normal_music()

        self.is_music_change = False
