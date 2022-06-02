from os import path

from mlgame.view.view_model import Scene
from .SingleMode import SingleMode
from .env import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, MAP_DIR
from ...TankMan.GameFramework.MyGame import GameFramework

'''need some fuction same as arkanoid which without dash in the name of fuction'''


class PacMan(GameFramework):
    def __init__(self, game_mode: str, map_no: int, time_limit: int, sound: str):
        super().__init__(map_no, time_limit, sound)
        self.scene = Scene(WINDOW_WIDTH, WINDOW_HEIGHT, BLACK)
        self.game_mode_name = game_mode
        self.game_mode = self.set_game_mode()

    def set_game_mode(self):
        map_path = path.join(MAP_DIR, self.map_name)
        if self.game_mode_name == "SINGLE":
            return SingleMode(map_path, self.time_limit, self.is_sound)
