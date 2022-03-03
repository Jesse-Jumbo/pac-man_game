import pygame

from mlgame.view.test_decorator import check_game_progress, check_game_result
from mlgame.view.view_model import create_text_view_data, create_asset_init_data, create_image_view_data, \
    create_line_view_data, Scene, create_polygon_view_data, create_rect_view_data
from mlgame.gamedev.game_interface import PaiaGame, GameResultState

from .env import *
from .sound_controller import *

from .GameMode import GameMode

'''need some fuction same as arkanoid which without dash in the name of fuction'''


class PacMan(PaiaGame):
    def __init__(self, user_num: int, game_mode: str, game_times, sound):
        super().__init__()
        self.game_times_goal = game_times
        self.game_times = 1
        self.score = []  # 用於計算積分
        self.is_sound = sound
        # self.sound_controller = SoundController(self.is_sound)
        self.game_type = game_mode
        self.user_num = user_num
        self.game_mode = self.set_game_mode()
        # self.game_mode.sound_controller.play_music()
        self.scene = Scene(WIDTH, HEIGHT, BLACK)
        self.attachements = []


    def game_to_player_data(self) -> dict:
        scene_info = self.get_scene_info
        to_player_data = {'1P': {'id': 0, 'x': 20, 'y': 160, 'status': 'GAME_ALIVE', 'distance': 0, 'velocity': 0, 'coin_num': 0, 'all_cars_pos': [(20, 160)], 'frame': 0, 'coin': []}}

        if to_player_data:
            return to_player_data
        else:
            return {
                "1P": scene_info,
                "2P": scene_info,
                "3P": scene_info,
                "4P": scene_info
            }

    @property
    def get_scene_info(self):
        """
        Get the scene information
        """
        scene_info = {'frame': self.game_mode.frame,
                      'status': self.game_mode.state,
                      'background': [WIDTH, HEIGHT],
                      'player_0_pos': self.game_mode.player.pos,
                      'ghosts_pos': [],
                      'game_result': self.game_mode.get_result()}

        for ghost in self.game_mode.ghosts:
            scene_info["ghost_pos"].append({ghost.ghost_no: ghost.pos})
        return scene_info

    def update(self, commands):
        self.frame_count += 1
        self.game_mode.run()
        self.game_result_state = "FAIL"
        if not self.is_running():
            if self.game_times < self.game_times_goal:
                self.game_times += 1
                return "RESET"
            else:
                return "QUIT"

    def reset(self):
        self.frame_count = 0

    def is_running(self):
        return self.game_mode.playing

    def get_scene_init_data(self) -> dict:
        """
        Get the scene and object information for drawing on the web
        """
        game_info = {'scene': self.scene.__dict__,
                     'assets': [{'type': 'image', 'image_id': 'computer_car', 'width': 60, 'height': 31, 'file_path': 'asset/image/pac_man_c.png', 'url': ''},
                                {'type': 'image', 'image_id': 'player1_car', 'width': 60, 'height': 31, 'file_path': 'asset/image/pac_man_c.png', 'url': ''},
                                {'type': 'image', 'image_id': 'background', 'width': 2000, 'height': 700, 'file_path': 'asset/image/pac_man_c.png', 'url': ''},
                                {'type': 'image', 'image_id': 'start_line', 'width': 45, 'height': 450, 'file_path': 'asset/image/pac_man_c.png', 'url': ''},
                                {'type': 'image', 'image_id': 'finish_line', 'width': 45, 'height': 450, 'file_path': 'asset/image/pac_man_c.png', 'url': ''},
                                {'type': 'image', 'image_id': 'info_km', 'width': 319, 'height': 80, 'file_path': 'asset/image/pac_man_c.png', 'url': ''}]}


        return game_info

    @check_game_progress
    def get_scene_progress_data(self) -> dict:
        """
        Get the position of src objects for drawing on the web
        """

        game_progress = {'background': [],
                         'object_list': [{'type': 'image', 'x': -2000, 'y': 0, 'width': 2000, 'height': 700, 'image_id': 'background', 'angle': 0},
                                         {'type': 'image', 'x': 0, 'y': 0, 'width': 2000, 'height': 700, 'image_id': 'background', 'angle': 0},
                                         {'type': 'image', 'x': 79, 'y': 100, 'width': 45, 'height': 428, 'image_id': 'start_line', 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -211, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -161, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -111, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -61, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -11, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 39, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 89, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 139, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 189, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 239, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 289, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 339, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 389, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 439, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 489, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 539, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 589, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 639, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 689, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 739, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 789, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 839, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 889, 'y': 149, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -211, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -161, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -111, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -61, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -11, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 39, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 89, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 139, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 189, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 239, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 289, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 339, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 389, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 439, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 489, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 539, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 589, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 639, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 689, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 739, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 789, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 839, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 889, 'y': 199, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -211, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -161, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -111, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -61, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -11, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 39, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 89, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 139, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 189, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 239, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 289, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 339, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 389, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 439, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 489, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 539, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 589, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 639, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 689, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 739, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 789, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 839, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 889, 'y': 249, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -211, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -161, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -111, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -61, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -11, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 39, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 89, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 139, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 189, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 239, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 289, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 339, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 389, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 439, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 489, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 539, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 589, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 639, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 689, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 739, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 789, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 839, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 889, 'y': 299, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -211, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -161, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -111, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -61, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -11, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 39, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 89, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 139, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 189, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 239, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 289, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 339, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 389, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 439, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 489, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 539, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 589, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 639, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 689, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 739, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 789, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 839, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 889, 'y': 349, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -211, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -161, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -111, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -61, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -11, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 39, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 89, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 139, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 189, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 239, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 289, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 339, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 389, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 439, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 489, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 539, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 589, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 639, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 689, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 739, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 789, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 839, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 889, 'y': 399, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -211, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -161, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -111, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -61, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -11, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 39, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 89, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 139, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 189, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 239, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 289, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 339, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 389, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 439, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 489, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 539, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 589, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 639, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 689, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 739, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 789, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 839, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 889, 'y': 449, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -211, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -161, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -111, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -61, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': -11, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 39, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 89, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 139, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 189, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 239, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 289, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 339, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 389, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 439, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 489, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 539, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 589, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 639, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 689, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 739, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 789, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 839, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'rect', 'name': 'lane', 'color': '#ffffff', 'x': 889, 'y': 499, 'width': 20, 'height': 3, 'angle': 0},
                                         {'type': 'image', 'x': 79, 'y': 100, 'width': 45, 'height': 428, 'image_id': 'start_line', 'angle': 0},
                                         {'type': 'image', 'x': 19, 'y': 160, 'width': 60, 'height': 30, 'image_id': 'player1_car', 'angle': 0}],
                         'toggle': [],
                         'foreground': [{'type': 'image', 'x': 685, 'y': 5, 'width': 319, 'height': 80, 'image_id': 'info_km', 'angle': 0},
                                        {'type': 'rect', 'name': 'block', 'x': 0, 'y': 650, 'angle': 0, 'width': 1000, 'height': 50, 'color': '#000000'},
                                        {'type': 'rect', 'name': 'user', 'x': 0, 'y': 666, 'angle': 0, 'width': 4, 'height': 4, 'color': '#ffffff'},
                                        {'type': 'text', 'content': '0m', 'color': '#ffffff', 'x': 725, 'y': 45, 'font-style': '20px Arial'}],
                         'user_info': [],
                         'game_sys_info': {}}

        return game_progress

    @check_game_result
    def get_game_result(self):
        """
        Get the src result for the web
        """

        return {"frame_used": self.frame_count,
                "state": self.game_result_state,
                "attachment": self.rank()
                }

    def get_keyboard_command(self):
        """
        Get the command according to the pressed keys
        """
        key_pressed_list = pygame.key.get_pressed()
        cmd_1P = []
        cmd_2P = []
        cmd_3P = []
        cmd_4P = []

        if key_pressed_list[pygame.K_LEFT]: cmd_1P.append(LEFT_cmd)
        if key_pressed_list[pygame.K_RIGHT]: cmd_1P.append(RIGHT_cmd)
        if key_pressed_list[pygame.K_UP]: cmd_1P.append(UP_cmd)
        if key_pressed_list[pygame.K_DOWN]: cmd_1P.append(DOWN_cmd)

        if key_pressed_list[pygame.K_a]: cmd_1P.append(LEFT_cmd)
        if key_pressed_list[pygame.K_d]: cmd_1P.append(RIGHT_cmd)
        if key_pressed_list[pygame.K_w]: cmd_1P.append(UP_cmd)
        if key_pressed_list[pygame.K_s]: cmd_1P.append(DOWN_cmd)

        if not self.is_running():
            return {"1P": "RESET",
                    "2P": "RESET",
                    "3P": "RESET",
                    "4P": "RESET",
                    }

        return {"1P": cmd_1P,
                "2P": cmd_2P,
                "3P": cmd_3P,
                "4P": cmd_4P,
                }

    @staticmethod
    def ai_clients():
        """
        let MLGame know how to parse your ai,
        you can also use this names to get different cmd and send different data to each ai client
        """
        return [
            {"name": "1P"},
            {"name": "2P"},
            {"name": "3P"},
            {"name": "4P"}
        ]

    def set_game_mode(self):
        if self.game_type == "NORMAL":
            game_mode = GameMode()
            return game_mode
        elif self.game_type == "RELIVE":
            pass

    def rank(self):
        # game_result = self.get_scene_info["game_result"]
        # TODO refactor
        # if len(self.attachements)==0:
        #     self.attachements = game_result
        #     for user in self.attachements:
        #         user["accumulated_score"] = 5 - user["single_rank"]
        #     return self.attachements
        #
        # for user in self.attachements:
        #     for single_rank in game_result:
        #         if single_rank['player'] == user['player']:
        #             match_single_rank = single_rank
        #     user["accumulated_score"] += (5 - match_single_rank["single_rank"])
        # if self.score:
        #     for user in self.score:
        #         user["accumulated_score"] += (5 - user["single_rank"])
        # else:
        #     self.score = single_game_result
        #     for user in self.score:
        #         user["accumulated_score"] = 5 - user["single_rank"]

        return self.attachements
