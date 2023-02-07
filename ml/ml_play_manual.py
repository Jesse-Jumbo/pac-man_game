"""
The template of the main script of the machine learning process
"""

import pygame


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        """
        Constructor

        @param ai_name A string "1P" or "2P" indicates that the `MLPlay` is used by
               which ai_name.
        """
        self.ai_name = ai_name
        print(f"Initial PacMan {ai_name} ml script")
        self.time = 0

    def update(self, scene_info: dict, keyboard=[], *args, **kwargs):
        """
        Generate the command according to the received scene information
        """
        # print(scene_info)
        # print(keyboard)
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        command = "NONE"
        if self.ai_name == "1P":
            if pygame.K_RIGHT in keyboard:
                command = "MOVE_RIGHT"
            elif pygame.K_LEFT in keyboard:
                command = "MOVE_LEFT"
            elif pygame.K_UP in keyboard:
                command = "MOVE_UP"
            elif pygame.K_DOWN in keyboard:
                command = "MOVE_DOWN"

        return [command]

    def reset(self):
        """
        Reset the status
        """
        print(f"reset PacMan {self.ai_name}")
