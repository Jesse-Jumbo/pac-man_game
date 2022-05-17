from GameFramework.MyGame import GameFramework
from mlgame.gamedev.game_interface import PaiaGame, GameStatus
from mlgame.view.test_decorator import check_game_result
from mlgame.view.view_model import create_text_view_data, create_asset_init_data, create_image_view_data, \
    Scene
from .SingleMode import SingleMode
from GameFramework.sound_controller import *


class PacMan(GameFramework):
    def __init__(self, game_mode: str, map_no: int, time_limit: int, sound: str):
        super().__init__(map_no, time_limit, sound)
        self.scene = Scene(WIDTH, HEIGHT, BLACK)
        self.game_mode_name = game_mode
        self.game_mode = self.set_game_mode()

    def set_game_mode(self):
        map_path = path.join(MAP_DIR, self.map_name)
        if self.game_mode_name == "SINGLE":
            return SingleMode(map_path, self.time_limit, self.is_sound)
