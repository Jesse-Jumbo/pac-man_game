from mlgame.game.paia_game import PaiaGame, GameStatus
from mlgame.view.view_model import Scene

from .SingleMode import SingleMode
from .env import *

MAP_WIDTH = 1000
MAP_HEIGHT = 600


class Game(PaiaGame):
    def __init__(self, user_num: int, game_mode: str, map_no: int, frame_limit: int, sound: str):
        super().__init__(user_num)
        self.is_paused = False
        self.is_debug = False
        self.is_sound = False

        self.game_mode_name = game_mode
        self.map_no = map_no
        self.frame_limit = frame_limit
        self.sound = sound
        if sound == "on":
            self.is_sound = True
        self.game_mode = self.set_game_mode()
        self.scene = Scene(width=self.game_mode.scene_width, height=self.game_mode.scene_height, color="#ffffff",
                           bias_y=50)

    def get_data_from_game_to_player(self) -> dict:
        to_players_data = self.game_mode.get_ai_data_to_player()
        return to_players_data

    def update(self, commands: dict):
        self.handle_event(commands)
        self.game_mode.debugging(self.is_debug)
        if not self.is_paused:
            self.frame_count += 1
            self.game_mode.update(commands)
            if not self.is_running():
                return "RESET"

    def reset(self):
        self.frame_count = 0
        self.game_mode.reset()
        self.rank()

    def get_scene_init_data(self) -> dict:
        """
        Get the scene and object information for drawing on the web
        """
        game_info = {'scene': self.scene.__dict__,
                     'assets': self.game_mode.get_init_image_data()}

        return game_info

    def get_scene_progress_data(self) -> dict:
        """
        Get the position of src objects for drawing on the web
        """
        scene_progress = {'background': [],
                          'object_list': [*self.get_obj_progress_data()],
                          'toggle_with_bias': [],
                          'toggle': self.game_mode.get_toggle_progress_data(),
                          'foreground': [],
                          'user_info': [],
                          'game_sys_info': {}}

        return scene_progress

    def get_obj_progress_data(self):
        obj_list = []
        for sprites in self.game_mode.obj_list:
            obj_list.extend(get_sprites_progress_data(sprites))
        obj_list.extend(self.game_mode.obj_rect_list)
        return obj_list

    def get_game_result(self):
        """
        Get the src result for the web
        """
        self.rank()
        return {"frame_used": self.frame_count,
                "state": self.game_result_state,
                "attachment": self.attachements
                }

    def is_running(self):
        return self.game_mode.status == GameStatus.GAME_ALIVE

    def rank(self):
        self.game_result_state = self.game_mode.state
        self.attachements = self.game_mode.get_player_result()
        return self.attachements

    def handle_event(self, commands):
        if ["DEBUG"] in commands.values():
            self.is_debug = not self.is_debug
        if ["PAUSED"] in commands.values():
            self.is_paused = not self.is_paused

    def set_game_mode(self):
        sound_path = ""
        if self.is_sound:
            sound_path = SOUND_DIR
        play_rect_area = pygame.Rect(0, 0, MAP_WIDTH, MAP_HEIGHT)
        if not self.game_mode_name == "SINGLE":
            return
        game_mode = SingleMode(
            map_path=MAP_DIR
            , map_no=self.map_no
            , frame_limit=self.frame_limit
            , sound_path=sound_path
            , play_rect_area=play_rect_area)
        return game_mode

def get_sprites_progress_data(sprites: pygame.sprite.Group):
    data_list = []
    for sprite in sprites:
        data = sprite.get_obj_progress_data()
        if data:
            data_list.append(data)
    return data_list
