import pygame.event

from mlgame.game.paia_game import GameResultState, GameStatus
from mlgame.view.view_model import create_asset_init_data, create_text_view_data, create_line_view_data

from .Dot import Dot
from .PowerPellet import PowerPellet
from .TiledMap import TiledMap
from .Wall import Wall
from .collide_hit_rect import *
from .env import *


class SingleMode:
    def __init__(self, map_path: str, map_no: int, frame_limit: int, sound_path: str, play_rect_area: pygame.Rect):
        # init game
        pygame.init()
        self.map_path = map_path
        self.map_no = map_no
        self.sound_path = sound_path
        self.map_name = f"map_0{map_no}.tmx"
        self.map = TiledMap(path.join(self.map_path, self.map_name))
        self.scene_width = self.map.map_width
        self.scene_height = self.map.map_height + 100
        self.width_center = self.scene_width // 2
        self.height_center = self.scene_height // 2
        self.play_rect_area = play_rect_area
        self.used_frame = 0
        self.state = GameResultState.FAIL
        self.status = GameStatus.GAME_ALIVE
        self.frame_limit = frame_limit
        self.obj_rect_list = []

        # control variables
        self.is_invincible = False
        self.is_through_wall = False
        # initialize sprites group
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.power_pellets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        # init obj data
        self.map.add_init_obj_data(PLAYER_IMG_NO, Player, play_rect_area=self.play_rect_area)
        self.map.add_init_obj_data(RED_GHOST_IMG_NO, Ghost, play_rect_area=self.play_rect_area)
        self.map.add_init_obj_data(PINK_GHOST_IMG_NO, Ghost, play_rect_area=self.play_rect_area)
        self.map.add_init_obj_data(GREEN_GHOST_IMG_NO, Ghost, play_rect_area=self.play_rect_area)
        self.map.add_init_obj_data(ORANGE_GHOST_IMG_NO, Ghost, play_rect_area=self.play_rect_area)
        self.map.add_init_obj_data(DOT_IMG_NO, Dot)
        self.map.add_init_obj_data(POWER_PELLET_IMG_NO, PowerPellet)
        for wall_no in WALLS_IMG_NO_LIST:
            self.map.add_init_obj_data(wall_no, Wall, play_rect_area=self.play_rect_area)
        # create obj
        all_obj = self.map.create_init_obj_dict()
        # init player
        self.player = all_obj[PLAYER_IMG_NO][0]
        self.all_sprites.add(self.player)
        # init red ghost
        self.red_ghost = all_obj[RED_GHOST_IMG_NO]
        self.ghosts.add(self.red_ghost)
        # init pink ghost
        self.pink_ghost = all_obj[PINK_GHOST_IMG_NO]
        self.ghosts.add(self.pink_ghost)
        # init green ghost
        self.green_ghost = all_obj[GREEN_GHOST_IMG_NO]
        self.ghosts.add(self.green_ghost)
        # init orange ghost
        self.orange_ghost = all_obj[ORANGE_GHOST_IMG_NO]
        self.ghosts.add(self.orange_ghost)
        self.all_sprites.add(*self.ghosts)
        # init walls
        for wall_no in WALLS_IMG_NO_LIST:
            self.walls.add(all_obj[wall_no])
        self.all_sprites.add(*self.walls)
        # init power pellets
        self.power_pellets.add(all_obj[POWER_PELLET_IMG_NO])
        self.all_sprites.add(*self.power_pellets)
        # init dots
        self.dots.add(all_obj[DOT_IMG_NO])
        self.all_sprites.add(*self.dots)
        # init pos list
        self.obj_list = [self.dots, self.power_pellets, [self.player], self.ghosts, self.walls]

    def update(self, command: dict):
        # refactor
        self.used_frame += 1
        self.check_collisions()
        self.player.update(command)
        self.ghosts.update()
        self.get_player_end()
        if self.used_frame >= self.frame_limit:
            self.get_game_end()

    def reset(self):
        # reset init game
        self.__init__(
            map_path=self.map_path
            , map_no=self.map_no
            , frame_limit=self.frame_limit
            , sound_path=self.sound_path
            , play_rect_area=self.play_rect_area)


    def get_player_end(self):
        if isinstance(self.player, Player) and self.player.is_alive:
            if not len(self.dots):
                self.set_result(state=GameResultState.FINISH, status=GameStatus.GAME_PASS)
        else:
            self.set_result(state=GameResultState.FAIL, status=GameStatus.GAME_OVER)

    def get_game_end(self):
        self.set_result(GameResultState.FINISH, GameStatus.GAME_DRAW)
        print("Time Out")

    def set_result(self, state: str, status: str):
        self.state = state
        self.status = status

    def get_player_result(self) -> list:
        """Define the end of game will return the player's info for user"""
        res = []
        if isinstance(self.player, Player):
            get_res = self.player.get_info_to_game_result()
            get_res["state"] = self.state
            get_res["status"] = self.status
            get_res["used_frame"] = self.used_frame
            res.append(get_res)
        return res

    def check_collisions(self):
        if not self.is_through_wall:
            collide_with_walls(self.player, self.walls)
        if not self.is_invincible:
            collide_player_with_ghosts(self.player, self.ghosts)
        collide_with_dots(self.player, self.dots)
        collide_with_dots(self.player, self.power_pellets)
        # ghost
        [collide_with_walls(ghost, self.walls) for ghost in self.ghosts]

    def get_init_image_data(self):
        init_image_data = []
        for act in PLAYER_IMG_PATH_DIC:
            for _id, img_path in PLAYER_IMG_PATH_DIC[act].items():
                init_image_data.append(create_asset_init_data(f"player_{act}_{_id}"
                                                              , TILE_X_SIZE, TILE_Y_SIZE
                                                              , img_path, PLAYER_IMAGE_URL[act][_id]))
        for act, img_path in RED_GHOST_IMAGE_PATH_DIC.items():
            init_image_data.append(create_asset_init_data(f"red_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in PINK_GHOST_IMAGE_PATH_DIC.items():
            init_image_data.append(create_asset_init_data(f"pink_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in GREEN_GHOST_IMAGE_PATH_DIC.items():
            init_image_data.append(create_asset_init_data(f"green_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in ORANGE_GHOST_IMAGE_PATH_DIC.items():
            init_image_data.append(create_asset_init_data(f"orange_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for act, img_path in BLUE_GHOST_IMAGE_PATH_DIC.items():
            init_image_data.append(create_asset_init_data(f"blue_ghost_{act}", TILE_X_SIZE,
                                                                                TILE_Y_SIZE, img_path, ""))
        for _id, img_path in WALLS_IMG_PATH_DIC.items():
            init_image_data.append(create_asset_init_data(f"wall_{_id}", TILE_X_SIZE, TILE_Y_SIZE,
                                                                                img_path, ""))
        init_image_data.append(create_asset_init_data("power_pellets", TILE_X_SIZE, TILE_Y_SIZE,
                                                                            POWER_PELLET_IMG_PATH, ""))
        init_image_data.append(create_asset_init_data("dots", TILE_X_SIZE, TILE_Y_SIZE,
                                                                            DOT_IMG_PATH, ""))
        return init_image_data

    def get_toggle_progress_data(self):
        toggle_data = []
        toggle_data.append(create_text_view_data(f"Score: {self.player.score}", WINDOW_WIDTH / 2 - 60, 0,
                                                                WHITE, "35px Arial BOLD"))
        toggle_data.append(create_text_view_data(f"Frame: {self.used_frame}", WINDOW_WIDTH - 130, 0,
                                                                WHITE, "35px Arial BOLD"))
        toggle_data.append(create_text_view_data(f"Lives: {self.player.lives}", 5, 0, WHITE,
                                                                "35px Arial BOLD"))
        return toggle_data

    def get_ai_data_to_player(self) -> dict:
        to_player_data = {}
        walls_info = [wall.get_data_from_obj_to_game() for wall in self.walls if isinstance(wall, Wall)]
        ghosts_info = [ghost.get_data_from_obj_to_game() for ghost in self.ghosts if isinstance(ghost, Ghost)]
        power_pellets_info = [power_pellet.get_data_from_obj_to_game() for power_pellet in self.power_pellets
                              if isinstance(power_pellet, PowerPellet)]
        dots_info = [dot.get_data_from_obj_to_game() for dot in self.dots if isinstance(dot, Dot)]
        if isinstance(self.player, Player):
            to_player_data = self.player.get_data_from_obj_to_game()
            to_player_data["used_frame"] = self.used_frame
            to_player_data["status"] = self.status
            to_player_data["walls_info"] = walls_info
            to_player_data["ghosts_info"] = ghosts_info
            to_player_data["power_pellets_info"] = power_pellets_info
            to_player_data["dots_info"] = dots_info

        return {"1P": to_player_data}

    def debugging(self, is_debug: bool):
        self.obj_rect_list = []
        if not is_debug:
            return
        play_rect_area_points = [self.play_rect_area.topleft, self.play_rect_area.topright
                                 , self.play_rect_area.bottomright, self.play_rect_area.bottomleft
                                 , self.play_rect_area.topleft]

        for sprite in self.all_sprites:
            if isinstance(sprite, pygame.sprite.Sprite):
                top_left = sprite.rect.topleft
                points = [top_left, sprite.rect.topright, sprite.rect.bottomright
                    , sprite.rect.bottomleft, top_left]
                for index in range(len(points) - 1):
                    self.obj_rect_list.append(create_line_view_data("rect", *points[index], *points[index + 1], RED))
                    self.obj_rect_list.append(create_line_view_data("play_rect_area", *play_rect_area_points[index]
                                                                    , *play_rect_area_points[index + 1], RED))

    def draw_foreground_data(self):
        all_text_data = [create_text_view_data(f"Score: {self.player.score}", WINDOW_WIDTH / 2 - 60, 0,
                                               WHITE, "35px Arial"),
                         create_text_view_data(f"Time: {self.frame_limit - self.used_frame}", WINDOW_WIDTH - 130, 0,
                                               WHITE, "35px Arial"),
                         create_text_view_data(f"Lives: {self.player.lives}", 5, 0, WHITE,
                                               "35px Arial")]
        return all_text_data
