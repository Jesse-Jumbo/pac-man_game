import pygame
from os import path
from .env import *

class SoundController():
    def __init__(self, is_sound_on):
        if is_sound_on == "on":
            self.is_sound_on = True
            try:
                pygame.mixer.init()
                self.count_time_sound = pygame.mixer.Sound(path.join(SOUND_DIR, "count_time.mp3"))
                self.blue_time_sound = pygame.mixer.Sound(path.join(SOUND_DIR, "blue_time.wav"))
                self.back_ground_sound = pygame.mixer.Sound(path.join(SOUND_DIR, "pacman background music.ogg"))
                # pygame.mixer.music.load(path.join(SOUND_DIR, "pacman background music.ogg"))
                pygame.mixer.music.set_volume(0.4)
            except Exception:
                self.is_sound_on = False

        else:
            self.is_sound_on = False

    def play_music(self):
        if self.is_sound_on:
            self.back_ground_sound.stop()
            self.count_time_sound.stop()
            self.blue_time_sound.stop()
            self.back_ground_sound.play()
            print("play_music")
        else:
            pass

    def play_count_time_sound(self):
        if self.is_sound_on:
            self.count_time_sound.stop()
            self.blue_time_sound.stop()
            self.back_ground_sound.stop()
            self.count_time_sound.play()
            print("play_count_time_sound")
        else:
            pass

    def play_blue_time_sound(self):
        if self.is_sound_on:
            self.blue_time_sound.stop()
            self.count_time_sound.stop()
            self.back_ground_sound.stop()
            self.blue_time_sound.play()
            print("play_blue_time_sound")
        else:
            pass

    def stop_play_sound(self):
        if self.is_sound_on:
            pass
