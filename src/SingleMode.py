import pygame.event

from .PacSoundController import PacSoundController
from ...TankMan.GameFramework.GameMode import GameMode
from games.PacMan.src.SquareGrid import *
from mlgame.gamedev.game_interface import GameResultState, GameStatus
from mlgame.view.view_model import create_asset_init_data, create_image_view_data, create_text_view_data
from .Dot import Dot, DOT_IMG_ID
from .GreenGhost import GreenGhost
from .OrangeGhost import OrangeGhost
from .PinkGhost import PinkGhost
from .PowerPellet import PowerPellet, PELLET_IMG_ID
from .RedGhost import RedGhost
from .collide_hit_rect import *
from .env import *
from ...TankMan.GameFramework.constants import ID, X, Y, ANGLE, HEIGHT, WIDTH


class SingleMode(GameMode):
    def __init__(self, map_path: str, time_limit: int, is_sound: bool):
        super().__init__(map_path, time_limit, is_sound)
        self.sound_controller = PacSoundController(is_sound)
        self.sound_controller.play_bgm()
        # control variables
        # initialize sprites group
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.power_pellets = pygame.sprite.Group()
        # init player
        player = self.map.create_obj_init_data(PLAYER_IMG_NO_LIST)[0]
        self.player = PacPlayer(player["_id"], player["_no"], player["x"], player["y"],
                                player["width"], player["height"])

        # init red ghost
        red_ghost = self.map.create_obj_init_data(RED_GHOST_IMG_NO_LIST)[0]
        self.red_ghost = RedGhost(red_ghost["_id"], red_ghost["_no"], red_ghost["x"], red_ghost["y"],
                                  red_ghost["width"], red_ghost["height"])
        self.ghosts.add(self.red_ghost)
        # init pink ghost
        pink_ghost = self.map.create_obj_init_data(PINK_GHOST_IMG_NO_LIST)[0]
        self.pink_ghost = PinkGhost(pink_ghost["_id"], pink_ghost["_no"], pink_ghost["x"], pink_ghost["y"],
                                    pink_ghost["width"], pink_ghost["height"])
        self.ghosts.add(self.pink_ghost)
        # init green ghost
        green_ghost = self.map.create_obj_init_data(GREEN_GHOST_IMG_NO_LIST)[0]
        self.green_ghost = GreenGhost(green_ghost["_id"], green_ghost["_no"], green_ghost["x"], green_ghost["y"],
                                      green_ghost["width"], green_ghost["height"])
        self.ghosts.add(self.green_ghost)
        # init orange ghost
        orange_ghost = self.map.create_obj_init_data(ORANGE_GHOST_IMG_NO_LIST)[0]
        self.orange_ghost = OrangeGhost(orange_ghost["_id"], orange_ghost["_no"], orange_ghost["x"], orange_ghost["y"],
                                        orange_ghost["width"], orange_ghost["height"])
        self.ghosts.add(self.orange_ghost)
        # init walls
        walls = self.map.create_obj_init_data(WALLS_IMG_NO_LIST)
        for wall in walls:
            pac_wall = PacWall(wall["_id"], wall["x"], wall["y"], wall["width"], wall["height"])
            self.walls.add(pac_wall)
        # init power pellets
        power_pellets = self.map.create_obj_init_data(POWER_PELLET_IMG_NO_LIST)
        for power_pellet in power_pellets:
            pac_power_pellet = PowerPellet(power_pellet["x"], power_pellet["y"], power_pellet["width"],
                                           power_pellet["height"])
            self.power_pellets.add(pac_power_pellet)
        # init dots
        dots = self.map.create_obj_init_data(DOT_IMG_NO_LIST)
        for dot in dots:
            pac_dot = Dot(dot["x"], dot["y"], dot["width"], dot["height"])
            self.dots.add(pac_dot)

        self.ghost_go_out_limit = len(self.dots)

    def get_result(self) -> list:
        res = [self.player.get_info()]
        return res

    def update_game_mode(self, command: dict):
        self.player.update(command["1P"])
        self.ghosts.update("")
        if self.used_frame in GHOST_GO_OUT_FRAME.values():
            self.sound_controller.play_ghost_sound()

    def check_game_is_end(self):
        if not len(self.dots):
            self.reset(state=GameResultState.FINISH, status=GameStatus.GAME_PASS)
        elif not self.player.is_alive:
            self.reset(state=GameResultState.FAIL, status=GameStatus.GAME_OVER)
        elif self.used_frame > self.frame_limit:
            self.reset(state=GameResultState.FAIL, status=GameStatus.GAME_OVER)
            print("Time Out")

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
                    self.is_debug = not self.is_debug
                if event.key == pygame.K_SPACE:
                    self.is_paused = not self.is_paused
                if event.key == pygame.K_m:
                    self.stop_music = not self.stop_music
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
                all_init_image_data.append(create_asset_init_data(f"player_{act}_{_id}", TILE_X_SIZE,
                                                                                    TILE_Y_SIZE, img_path,
                                                                                    PLAYER_IMAGE_URL[act][_id]))
        for act, img_path in RED_GHOST_IMAGE_PATH_DIC.items():
            all_init_image_data.append(create_asset_init_data(f"red_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in PINK_GHOST_IMAGE_PATH_DIC.items():
            all_init_image_data.append(create_asset_init_data(f"pink_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in GREEN_GHOST_IMAGE_PATH_DIC.items():
            all_init_image_data.append(create_asset_init_data(f"green_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in ORANGE_GHOST_IMAGE_PATH_DIC.items():
            all_init_image_data.append(create_asset_init_data(f"orange_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in BLUE_GHOST_IMAGE_PATH_DIC.items():
            all_init_image_data.append(create_asset_init_data(f"blue_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for _id, img_path in WALLS_IMG_PATH_DIC.items():
            all_init_image_data.append(create_asset_init_data(f"wall_{_id}", TILE_X_SIZE, TILE_Y_SIZE,
                                                                                img_path, ""))
        all_init_image_data.append(create_asset_init_data(PELLET_IMG_ID, TILE_X_SIZE, TILE_Y_SIZE,
                                                                            POWER_PELLET_IMG_PATH, ""))
        all_init_image_data.append(create_asset_init_data(DOT_IMG_ID, TILE_X_SIZE, TILE_Y_SIZE,
                                                                            DOT_IMG_PATH, ""))

        return all_init_image_data

    def draw_sprite_data(self):
        all_sprite_data = []
        for dot in self.dots:
            if isinstance(dot, Dot):
                data = dot.get_image_data()
                all_sprite_data.append(create_image_view_data(data[ID], data[X], data[Y], data[WIDTH], data[HEIGHT],
                                                              data[ANGLE]))

        for power_pellet in self.power_pellets:
            if isinstance(power_pellet, PowerPellet):
                data = power_pellet.get_image_data()
                all_sprite_data.append(create_image_view_data(data[ID], data[X], data[Y], data[WIDTH], data[HEIGHT],
                                                              data[ANGLE]))

        data = self.player.get_image_data()
        all_sprite_data.append(create_image_view_data(data[ID], data[X], data[Y], data[WIDTH], data[HEIGHT],
                                                      data[ANGLE]))

        for ghost in self.ghosts:
            if isinstance(ghost, Ghost):
                data = ghost.get_image_data()
                all_sprite_data.append(create_image_view_data(data[ID], data[X], data[Y], data[WIDTH], data[HEIGHT],
                                                              data[ANGLE]))

        for wall in self.walls:
            if isinstance(wall, PacWall):
                data = wall.get_image_data()
                all_sprite_data.append(create_image_view_data(data[ID], data[X], data[Y], data[WIDTH], data[HEIGHT],
                                                              data[ANGLE]))

        return all_sprite_data

    def draw_text_data(self):
        all_text_data = []
        all_text_data.append(create_text_view_data(f"Score: {self.player.score}", WINDOW_WIDTH / 2 - 60, 0,
                                                                WHITE, "35px Arial"))
        all_text_data.append(create_text_view_data(f"Time: {(self.used_frame // 60)}", WINDOW_WIDTH - 130, 0,
                                                                WHITE, "35px Arial"))
        all_text_data.append(create_text_view_data(f"Lives: {self.player.lives}", 5, 0, WHITE,
                                                                "35px Arial"))
        return all_text_data

    def create_scene_info(self):
        scene_info = {"frame": self.used_frame,
                      "status": self.status,
                      "background": [WINDOW_WIDTH, WINDOW_HEIGHT],
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
