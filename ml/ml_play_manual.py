"""
The template of the main script of the machine learning process
"""

import pygame

from src.env import LEFT_CMD, RIGHT_CMD, UP_CMD, DOWN_CMD


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
            if pygame.K_LEFT in keyboard:
                command = LEFT_CMD
            elif pygame.K_RIGHT in keyboard:
                command = RIGHT_CMD
            elif pygame.K_UP in keyboard:
                command = UP_CMD
            elif pygame.K_DOWN in keyboard:
                command = DOWN_CMD
            if pygame.K_b in keyboard:
                command = "DEBUG"
            if pygame.K_p in keyboard:
                command = "PAUSED"

        return [command]

    def reset(self):
        """
        Reset the status
        """
        print(f"reset PacMan {self.ai_name}")
