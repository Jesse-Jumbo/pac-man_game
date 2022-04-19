import pygame
from os import path
from .env import *

class SoundController():
    def __init__(self, is_sound_on):
        if is_sound_on == "on":
            self.is_sound_on = True
            try:
                pygame.mixer.init()
                self.warn_sound = pygame.mixer.Sound(path.join(SOUND_DIR, "count_time.mp3"))
            except Exception as e:
                self.is_sound_on = False
                print(f"sound_error:{e}")
        else:
            self.is_sound_on = False

    def play_normal_music(self):
        if self.is_sound_on:
            pygame.mixer.init()
            pygame.mixer.music.load(path.join(SOUND_DIR, "pacman background music.ogg"))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
        else:
            pass

    def play_danger_music(self):
        if self.is_sound_on:
            pygame.mixer.init()
            pygame.mixer.music.load(path.join(SOUND_DIR, "count_time.mp3"))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
        else:
            pass

    def play_blue_music(self):
        if self.is_sound_on:
            pygame.mixer.init()
            pygame.mixer.music.load(path.join(SOUND_DIR, "blue_time.wav"))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
            print("blue_music")
        else:
            pass

    def play_warn_sound(self):
        if self.is_sound_on:
            # pygame.mixer.music.pause()
            self.warn_sound.play(maxtime=1800).set_volume(0.2)
        else:
            pass
