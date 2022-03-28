class MLPlay:
    def __init__(self):
        self.game_info = []
        self.player_info = []
        self.ghost_info = []
        print("Initial ml script")

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        print(scene_info)
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        return "MOVE_RIGHT"

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")

