from games.PacMan.src.env import FPS, GHOST_SND, INVINCIBILITY_MUSIC, BGM
from games.TankMan.GameFramework.sound_controller import SoundController


class PacSoundController(SoundController):
    def play_bgm(self):
        self.play_music(BGM, 0.2)

    def play_invincibility_sound(self):
        self.play_music(INVINCIBILITY_MUSIC, 0.2)

    def play_ghost_sound(self):
        self.play_sound(GHOST_SND, 0.6, int(3.5 * FPS))
