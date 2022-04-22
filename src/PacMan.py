from mlgame.gamedev.game_interface import PaiaGame, GameStatus
from mlgame.view.test_decorator import check_game_result
from mlgame.view.view_model import create_text_view_data, create_asset_init_data, create_image_view_data, \
    Scene
from .GameMode import GameMode
from .sound_controller import *

'''need some fuction same as arkanoid which without dash in the name of fuction'''


class PacMan(PaiaGame):
    def __init__(self, user_num: int, game_mode: str, map_no: int, sound: str):
        super().__init__()
        self.scene = Scene(WIDTH, HEIGHT, BLACK)
        # self.game_times = 1
        self.is_sound = sound
        # TODO figure out why can't delete sound_controller
        self.sound_controller = SoundController(self.is_sound)
        self.game_type = game_mode
        self.user_num = user_num
        self.map = f"map0{map_no}.tmx"
        self.game_mode = self.set_game_mode(self.map)
        self.attachements = []

    # TODO refactor AI need data (what is player data)
    def game_to_player_data(self) -> dict:
        scene_info = self.get_scene_info
        to_player_data = {}
        player_data = self.game_mode.player.get_info()
        player_data["frame"] = scene_info["frame"]
        player_data["status"] = scene_info["status"]
        player_data["dots_pos"] = []
        player_data["power_pellets_pos"] = []
        player_data["walls_pos"] = []

        for ghost in self.game_mode.ghosts:
            player_data[ghost.ghost_no] = ghost.pos
        for dot in self.game_mode.dots:
            player_data["dots_pos"].append(dot.rect.center)
        for power_pellet in self.game_mode.power_pellets:
            player_data["power_pellets_pos"].append(power_pellet.rect.center)
        for wall in self.game_mode.walls:
            player_data["walls_pos"].append(wall.pos)

        to_player_data[player_data['player_id']] = player_data
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
                      'status': self.game_mode.status,
                      'background': [WIDTH, HEIGHT],
                      f'player_{self.game_mode.player.player_no}_pos': self.game_mode.player.pos,
                      'ghosts_pos': [],
                      'game_result': self.game_mode.get_result(),
                      'state': self.game_mode.state}

        for ghost in self.game_mode.ghosts:
            scene_info["ghosts_pos"].append({ghost.ghost_no: ghost.pos})
        return scene_info

    def update(self, commands: dict):
        self.frame_count += 1
        self.game_mode.run(commands)
        if not self.is_running():
            return "RESET"

    def reset(self):
        self.frame_count = 0
        self.game_mode = self.set_game_mode(self.map)
        # TODO play music
        # self.game_mode.sound_controller.player_music()

    def is_running(self):
        if self.game_mode.status == GameStatus.GAME_ALIVE:
            return True
        else:
            return False

    def get_scene_init_data(self) -> dict:
        """
        Get the scene and object information for drawing on the web
        """
        game_info = {'scene': self.scene.__dict__,
                     'assets': []}

        # initialize player image
        for key, values in self.game_mode.player.image_dic.items():
            for i in range(4):
                game_info['assets'].append(
                    create_asset_init_data(
                        f'player{self.game_mode.player.player_no}P_{key}_{i}'
                        , TILE_X_SIZE, TILE_Y_SIZE, values[i], ""))
        # initialize ghosts image
        for ghost in self.game_mode.ghosts:
            for key, value in ghost.ghosts_images[ghost.ghost_image_no].items():
                game_info['assets'].append(
                    create_asset_init_data(
                        f"{ghost.ghost_no}_{key}", TILE_X_SIZE, TILE_Y_SIZE, value, ""))
        # initialize blue ghost image
        for key, value in self.game_mode.red_ghost.ghosts_images[BLUE_IMG].items():
            game_info['assets'].append(create_asset_init_data(f"{BLUE_GHOST_NO}_{key}", TILE_X_SIZE, TILE_Y_SIZE,
                                                              value, ""))
        # initialize dots image
        for i in range(len(self.game_mode.dots)):
            game_info["assets"].append(create_asset_init_data("dots", TILE_X_SIZE, TILE_Y_SIZE,
                                                              path.join(IMAGE_DIR, DOT_IMG), ""))
        # initialize power_pellets image
        for i in range(len(self.game_mode.power_pellets)):
            game_info["assets"].append(create_asset_init_data("power_pellets", TILE_X_SIZE, TILE_Y_SIZE,
                                                              path.join(IMAGE_DIR, POWER_PELLET_IMG), ""))
        # initialize walls image
        for wall in self.game_mode.walls:
            game_info["assets"].append(create_asset_init_data(f"wall_{wall.obj_no}", TILE_X_SIZE, TILE_Y_SIZE,
                                                              path.join(IMAGE_DIR, wall.img_path), ""))

        return game_info

    # @check_game_progress
    def get_scene_progress_data(self) -> dict:
        """
        Get the position of src objects for drawing on the web
        """

        game_progress = {'background': [],
                         'object_list': [],
                         'toggle': [],
                         'foreground': [],
                         'user_info': [],
                         'game_sys_info': {}}

        # update player image
        game_progress["object_list"].append(create_image_view_data(self.game_mode.player.image_path,
                                                                   self.game_mode.player.rect.x,
                                                                   self.game_mode.player.rect.y,
                                                                   TILE_X_SIZE, TILE_Y_SIZE))
        # update ghosts image
        for ghost in self.game_mode.ghosts:
            game_progress["object_list"].append(create_image_view_data(ghost.image_no,
                                                                       ghost.rect.x, ghost.rect.y,
                                                                       TILE_X_SIZE, TILE_Y_SIZE))
        # update dots image
        for dot in self.game_mode.dots:
            game_progress["object_list"].append(create_image_view_data('dots',
                                                                       dot.rect.x, dot.rect.y,
                                                                       TILE_X_SIZE, TILE_Y_SIZE))
        # update power_pellets image
        for power_pellet in self.game_mode.power_pellets:
            game_progress["object_list"].append(create_image_view_data('power_pellets',
                                                                       power_pellet.rect.x, power_pellet.rect.y,
                                                                       TILE_X_SIZE, TILE_Y_SIZE))
        # update walls image
        for wall in self.game_mode.walls:
            game_progress["object_list"].append(create_image_view_data(f'wall_{wall.obj_no}',
                                                                       wall.rect.x, wall.rect.y,
                                                                       TILE_X_SIZE, TILE_Y_SIZE))
        # update score text
        game_progress["foreground"].append(create_text_view_data(f"Score: {self.game_mode.player.score}",
                                                                 WIDTH / 2 - 30, 0, WHITE, "20px Arial"))
        # update frame text
        game_progress["foreground"].append(create_text_view_data(f"Time: {(self.game_mode.frame // 60)}",
                                                                 WIDTH - 90, 0, WHITE, "20px Arial"))

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
        # TODO 此處回傳的資料 要與 ml_play.py 一致
        cmd_1P = ""
        cmd_2P = ""
        cmd_3P = ""
        cmd_4P = ""

        if key_pressed_list[pygame.K_UP] or key_pressed_list[pygame.K_w] or key_pressed_list[pygame.K_KP_8]:
            cmd_1P = UP_cmd
        elif key_pressed_list[pygame.K_RIGHT] or key_pressed_list[pygame.K_d]:
            cmd_1P = RIGHT_cmd
        elif key_pressed_list[pygame.K_LEFT] or key_pressed_list[pygame.K_a]:
            cmd_1P = LEFT_cmd
        elif key_pressed_list[pygame.K_DOWN] or key_pressed_list[pygame.K_s]:
            cmd_1P = DOWN_cmd

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

    def set_game_mode(self, map_name: str):
        if self.game_type == "NORMAL":
            game_mode = GameMode(map_name, self.sound_controller)
            return game_mode
        elif self.game_type == "RELIVE":
            pass

    def rank(self):
        self.game_result_state = self.game_mode.state
        game_result = self.game_mode.get_result()
        self.attachements = game_result

        return self.attachements
