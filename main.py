import pygame
from src import RacingCar

from src.env import FPS
from mlgame.view.view import PygameView
from mlgame.gamedev.generic import quit_or_esc

if __name__ == '__main__':
    pygame.init()
    # game = RacingCar.RacingCar(user_num=2, game_mode="NORMAL", car_num=50, racetrack_length=10000, game_times=1, sound="off")
    game = RacingCar.PacMan(user_num=1, game_mode="RELIVE", car_num=0, racetrack_length=1000, game_times=1, sound="off")
    scene_init_info_dict = game.get_scene_init_data()
    game_view = PygameView(scene_init_info_dict)
    interval = 1 / 30
    frame_count = 0
    while game.isRunning() and not quit_or_esc():
        pygame.time.Clock().tick_busy_loop(FPS)
        game.update(game.get_keyboard_command())
        game_progress_data = game.get_scene_progress_data()
        game_view.draw_screen()
        game_view.draw(game_progress_data)
        game_view.flip()
        if frame_count == 1:
            print(game_progress_data["foreground"])
        frame_count += 1

    pygame.quit()

# if __name__ == '__main__':
#     pygame.init()
#     # game = RacingCar.RacingCar(user_num=2, game_mode="NORMAL", car_num=50, racetrack_length=10000, game_times=1, sound="off")
#     game = RacingCar.RacingCar(user_num=4, game_mode="RELIVE", car_num=20, racetrack_length=1000, game_times=1, sound="off")
#     # game = RacingCar.RacingCar(2, "COIN", 30, 1, "off")
#     scene_init_info_dict = game.get_scene_init_data()
#     game_view = PygameView(scene_init_info_dict)
#     interval = 1 / 30
#     frame_count = 0
#     while game.isRunning() and not quit_or_esc():
#         pygame.time.Clock().tick_busy_loop(FPS)
#         game.update(game.get_keyboard_command())
#         game_progress_data = game.get_scene_progress_data()
#         game_view.draw_screen()
#         game_view.draw(game_progress_data)
#         game_view.flip()
#         frame_count += 1
#
#     pygame.quit()
