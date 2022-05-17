import pygame.event

from GameFramework.GameMode import GameMode
from games.PacMan.src.SquareGrid import *
from mlgame.gamedev.game_interface import GameResultState, GameStatus
from .Dot import Dot, DOT_IMG_ID
from .Ghost import Ghost
from .PacPlayer import PacPlayer
from .PowerPellet import PowerPellet, PELLET_IMG_ID
from .collide_hit_rect import *
from .env import *


class SingleMode(GameMode):
    # TODO class type? object? for SoundController
    def __init__(self, map_path: str, time_limit: int, is_sound: bool):
        super().__init__(map_path, time_limit, is_sound)
        # initialize all variables and so all the setup for a new game
        self.time_limit = time_limit
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        # control variables
        self.draw_debug = False
        self.check_path = False
        self.is_blue_ghost = False
        self.is_danger = False
        self.is_warn = False
        self.stop_music = False
        self.is_music_change = False
        # load all img and music data from folder
        # initialize sprites group
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.power_pellets = pygame.sprite.Group()
        self.nodes = pygame.sprite.Group()
        # create map object
        player = self.map.create_obj_init_data(PLAYER_IMG_NO_LIST)[0]
        self.player = PacPlayer(player["_id"], player["_no"], player["x"], player["y"],
                                player["width"], player["height"])
        red_ghost = self.map.create_obj_init_data(RED_GHOST_IMG_NO_LIST)[0]
        self.red_ghost = Ghost(red_ghost["_id"], red_ghost["_no"], red_ghost["x"], red_ghost["y"],
                               red_ghost["width"], red_ghost["height"])
        pink_ghost = self.map.create_obj_init_data(PINK_GHOST_IMG_NO_LIST)[0]
        self.pink_ghost = Ghost(pink_ghost["_id"], pink_ghost["_no"], pink_ghost["x"], pink_ghost["y"],
                                pink_ghost["width"], pink_ghost["height"])
        green_ghost = self.map.create_obj_init_data(GREEN_GHOST_IMG_NO_LIST)[0]
        self.green_ghost = Ghost(green_ghost["_id"], green_ghost["_no"], green_ghost["x"], green_ghost["y"],
                                 green_ghost["width"], green_ghost["height"])
        orange_ghost = self.map.create_obj_init_data(ORANGE_GHOST_IMG_NO_LIST)[0]
        self.orange_ghost = Ghost(orange_ghost["_id"], orange_ghost["_no"], orange_ghost["x"], orange_ghost["y"],
                                  orange_ghost["width"], orange_ghost["height"])
        walls = self.map.create_obj_init_data(WALLS_IMG_NO_LIST)
        for wall in walls:
            pac_wall = PacWall(wall["_id"], wall["x"], wall["y"], wall["width"], wall["height"])
            self.walls.add(pac_wall)
        power_pellets = self.map.create_obj_init_data(POWER_PELLET_IMG_NO_LIST)
        for power_pellet in power_pellets:
            pac_power_pellet = PowerPellet(power_pellet["x"], power_pellet["y"], power_pellet["width"],
                                           power_pellet["height"])
            self.power_pellets.add(pac_power_pellet)
        dots = self.map.create_obj_init_data(DOT_IMG_NO_LIST)
        for dot in dots:
            pac_dot = Dot(dot["x"], dot["y"], dot["width"], dot["height"])
            self.dots.add(pac_dot)

        self.ghosts.add(self.red_ghost)
        self.ghosts.add(self.pink_ghost)
        self.ghosts.add(self.green_ghost)
        self.ghosts.add(self.orange_ghost)

        self.ghost_go_out_limit = len(self.dots)

    def get_result(self) -> list:
        res = [{"1P": self.player.get_info()}]
        return res

    def game_update(self, command: dict):
        if not self.is_paused:
            self.player.update(command["1P"])
            self.ghosts.update("")
            if self.used_frame in GHOST_GO_OUT_FRAME.values():
                self.sound_controller.play_sound(DANGER_SND, volume=0.2, max_time=1800)

    def reset(self):
        if len(self.dots) == 0:
            self.state = GameResultState.FINISH
            self.status = GameStatus.GAME_PASS
        if not self.player.is_alive:
            self.state = GameResultState.FAIL
            self.status = GameStatus.GAME_OVER
        if self.used_frame > self.time_limit:
            self.state = GameResultState.FAIL
            self.status = GameStatus.GAME_OVER

    def check_events(self):
        # catch all events here
        cmd_1P = ""
        key_pressed_list = pygame.key.get_pressed()
        if key_pressed_list[pygame.K_UP]:
            cmd_1P = UP_cmd
        elif key_pressed_list[pygame.K_DOWN]:
            cmd_1P = DOWN_cmd
        elif key_pressed_list[pygame.K_RIGHT]:
            cmd_1P = RIGHT_cmd
        elif key_pressed_list[pygame.K_LEFT]:
            cmd_1P = LEFT_cmd

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    self.draw_debug = not self.draw_debug
                if event.key == pygame.K_SPACE:
                    self.is_paused = not self.is_paused
                if event.key == pygame.K_m:
                    self.stop_music = not self.stop_music
                # check ghost search path
                if event.key == pygame.K_r:
                    pass
                    # self.red_ghost.draw_check_path = not self.red_ghost.draw_check_path
                if event.key == pygame.K_k:
                    pass
                    # self.pink_ghost.draw_check_path = not self.pink_ghost.draw_check_path
                if event.key == pygame.K_o:
                    pass
                    # self.orange_ghost.draw_check_path = not self.orange_ghost.draw_check_path
                if event.key == pygame.K_g:
                    pass
                    # self.green_ghost.draw_check_path = not self.green_ghost.draw_check_path
        return {"1P": cmd_1P}

    def check_collisions(self):
        # for player
        collide_with_walls(self.player, self.walls)
        collide_player_with_ghosts(self.player, self.ghosts)
        collide_with_dots(self.player, self.dots)
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

        # for ghost
        for ghost in self.ghosts:
            collide_with_walls(ghost, self.walls)

    def create_init_image_data(self):
        all_init_image_data = []
        for act in PLAYER_IMG_PATH_DIC:
            for _id, img_path in PLAYER_IMG_PATH_DIC[act].items():
                all_init_image_data.append(self.data_creator.create_image_init_data(f"player_{act}_{_id}", TILE_X_SIZE,
                                                                                    TILE_Y_SIZE, img_path,
                                                                                    PLAYER_IMAGE_URL[act][_id]))
        for act, img_path in RED_GHOST_IMAGE_PATH_DIC.items():
            all_init_image_data.append(self.data_creator.create_image_init_data(f"red_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in PINK_GHOST_IMAGE_PATH_DIC.items():
            all_init_image_data.append(self.data_creator.create_image_init_data(f"pink_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in GREEN_GHOST_IMAGE_PATH_DIC.items():
            all_init_image_data.append(self.data_creator.create_image_init_data(f"green_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in ORANGE_GHOST_IMAGE_PATH_DIC.items():
            all_init_image_data.append(self.data_creator.create_image_init_data(f"orange_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in BLUE_GHOST_IMAGE_PATH_DIC.items():
            all_init_image_data.append(self.data_creator.create_image_init_data(f"blue_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for _id, img_path in WALLS_IMG_PATH_DIC.items():
            all_init_image_data.append(self.data_creator.create_image_init_data(f"wall_{_id}", TILE_X_SIZE, TILE_Y_SIZE,
                                                                                img_path, ""))
        all_init_image_data.append(self.data_creator.create_image_init_data(PELLET_IMG_ID, TILE_X_SIZE, TILE_Y_SIZE,
                                                                            POWER_PELLET_IMG_PATH, ""))
        all_init_image_data.append(self.data_creator.create_image_init_data(DOT_IMG_ID, TILE_X_SIZE, TILE_Y_SIZE,
                                                                            DOT_IMG_PATH, ""))

        return all_init_image_data

    def draw_sprite_data(self):
        all_sprite_data = []
        for dot in self.dots:
            if isinstance(dot, Dot):
                all_sprite_data.append(dot.get_image_data())
        for power_pellet in self.power_pellets:
            if isinstance(power_pellet, PowerPellet):
                all_sprite_data.append(power_pellet.get_image_data())
        all_sprite_data.append(self.player.get_image_data())
        for ghost in self.ghosts:
            if isinstance(ghost, Ghost):
                all_sprite_data.append(ghost.get_image_data())
        for wall in self.walls:
            if isinstance(wall, PacWall):
                all_sprite_data.append(wall.get_image_data())

        return all_sprite_data

    def draw_text_data(self):
        all_text_data = []
        all_text_data.append(self.data_creator.create_text_data(f"Score: {self.player.score}", WIDTH / 2 - 30, 0,
                                                                WHITE, "20px Arial"))
        all_text_data.append(self.data_creator.create_text_data(f"Time: {(self.used_frame // 60)}", WIDTH - 90, 0,
                                                                WHITE, "20px Arial"))
        return all_text_data

    def create_scene_info(self):
        scene_info = {"frame": self.used_frame,
                      "status": self.status,
                      "background": [WIDTH, HEIGHT],
                      "walls_xy_pos": [],
                      "power_pellets_xy_pos": [],
                      "dots_xy_pos": [],
                      "ghosts_xy_pos": [],
                      "Player_xy_pos": self.player.get_xy_pos(),
                      "game_result": self.get_result(),
                      "state": self.state}
        for wall in self.walls:
            if isinstance(wall, PacWall):
                scene_info["walls_xy_pos"].append(wall.get_xy_pos())
        for power_pellet in self.power_pellets:
            if isinstance(power_pellet, PowerPellet):
                scene_info["walls_xy_pos"].append(power_pellet.get_xy_pos())
        for dot in self.dots:
            if isinstance(dot, Dot):
                scene_info["walls_xy_pos"].append(dot.get_xy_pos())
        for ghost in self.ghosts:
            if isinstance(ghost, Ghost):
                scene_info["walls_xy_pos"].append(ghost.get_xy_pos())

        return scene_info

    def create_game_data_to_player(self):
        to_player_data = {}
        info = self.player.get_info()
        info["used_frame"] = self.used_frame
        info["status"] = self.status
        walls_info = []
        for wall in self.walls:
            if isinstance(wall, PacWall):
                walls_info.append(wall.get_info())
        info["walls_info"] = walls_info
        power_pellets_info = []
        for power_pellets in self.power_pellets:
            if isinstance(power_pellets, PowerPellet):
                power_pellets_info.append(power_pellets.get_info())
        info["power_pellets_info"] = power_pellets_info
        dots_info = []
        for dot in self.dots:
            if isinstance(dot, Dot):
                dots_info.append(dot.get_info())
        info["dots_info"] = dots_info
        ghosts_info = []
        for ghost in self.ghosts:
            if isinstance(ghost, Ghost):
                ghosts_info.append(ghost.get_info())
        info["ghosts_info"] = ghosts_info

        to_player_data["1P"] = info
        return to_player_data
