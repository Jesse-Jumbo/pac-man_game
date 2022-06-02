import random


class MLPlay:
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        print("Initial PacMan ml script 1P")
        self.side = side
        self.time = 0

    def update(self, scene_info: dict, *args, **kwargs):
        """
        Generate the command according to the received scene information
        """
        # print(scene_info)
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        command = []
        act = None
        self.time += 1
        if self.time % 30 == 0:
            act = random.randrange(5)

        if act == 1:
            command.append("TURN_RIGHT")
        elif act == 2:
            command.append("TURN_LEFT")
        elif act == 3:
            command.append("FORWARD")
        elif act == 4:
            command.append("BACKWARD")
        if act == 0:
            command.append("SHOOT")

        return command

    def reset(self):
        """
        Reset the status
        """
        print(f"reset PacMan {self.side}")
