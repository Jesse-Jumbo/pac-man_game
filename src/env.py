from os import path

import pygame

'''width and height'''
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

'''environment data'''
FPS = 60
'''color'''
BLACK = "#000000"
WHITE = "#ffffff"
RED = "#ff0000"
YELLOW = "#ffff00"
GREEN = "#00ff00"
GREY = "#8c8c8c"
BLUE = "#0000ff"
LIGHT_BLUE = "#21A1F1"
CYAN_BLUE = "#00FFFF"
PINK = "#FF00FF"
DARKGREY = "#282828"
LIGHTGREY = "#646464"
BROWN = "#643705"
FOREST = "#22390A"
MAGENTA = "#FF00FF"
MEDGRAY = "#4B4B4B"

'''command'''
LEFT_CMD = "MOVE_LEFT"
RIGHT_CMD = "MOVE_RIGHT"
UP_CMD = "MOVE_UP"
DOWN_CMD = "MOVE_DOWN"

'''data path'''
GAME_DIR = path.dirname(__file__)
MAP_DIR = path.join(GAME_DIR, "..", "asset", "maps")
SOUND_DIR = path.join(GAME_DIR, "..", "asset", "sound")
IMAGE_DIR = path.join(GAME_DIR, "..", "asset", "image")

'''BG View'''
TITLE = "Pac-Man!"
BG_COLOR = DARKGREY
TILE_X_SIZE = 50
TILE_Y_SIZE = 50
TILE_SIZE = 50
GRID_WIDTH = WINDOW_WIDTH / TILE_X_SIZE
GRID_HEIGHT = WINDOW_HEIGHT / TILE_Y_SIZE

'''window pos'''
WIDTH_CENTER = WINDOW_WIDTH / 2
HEIGHT_CENTER = WINDOW_HEIGHT / 2

'''object size'''
ALL_OBJECT_SIZE = pygame.Rect(0, 0, TILE_X_SIZE - 2, TILE_Y_SIZE - 2)

"""all setting"""
DOWN_IMG = 'down'
RIGHT_IMG = 'right'
UP_IMG = 'up'
LEFT_IMG = 'left'

"""collide setting"""
WITH_GHOST = 'ghost'
WITH_PLAYER = 'player'
DOT_SCORE = 10
POWER_PELLET_SCORE = 50
BLUE_GHOST_SCORE = 200
CHERRY_SCORE = 500

'''player setting'''
PLAYER_SPEED = 5.0
PLAYRE_HIT_RECT = pygame.Rect(0, 0, TILE_X_SIZE - 2, TILE_Y_SIZE - 2)

'''ghost setting'''
GHOST_HIT_RECT = pygame.Rect(0, 0, TILE_X_SIZE - 2, TILE_Y_SIZE - 2)
GHOST_SPEED = 3.0
SPEED_SLOW = - 0.2
BLUE_IMG = 'blue_ghost_img'
RED_IMG = 'red_ghost_img'
PINK_IMG = 'pink_ghost_img'
GREEN_IMG = 'green_ghost_img'
ORANGE_IMG = 'orange_ghost_img'
BLUE_LIMIT = 10000
RED_GHOST_NO = "red_ghost"
PINK_GHOST_NO = "pink_ghost"
GREEN_GHOST_NO = "green_ghost"
ORANGE_GHOST_NO = "orange_ghost"
BLUE_GHOST_NO = "blue_ghost"
GHOST_NO_LIST = [RED_GHOST_NO, PINK_GHOST_NO, GREEN_GHOST_NO, ORANGE_GHOST_NO]

"""ghost go out frame"""
GHOST_GO_OUT_FRAME = {"red": 60, "pink": 480, "green": 900, "orange": 1200}

'''wall setting'''
WALL_IMG = "wall.png"

'''dot setting'''
DOT_HIT_RECT = pygame.Rect(0, 0, 5, 5)

'''Power Pellets setting'''
POWER_PELLET_HIT_RECT = pygame.Rect(0, 0, 8, 8)

'''node setting'''
NODE_HIT_RECT = pygame.Rect(0, 0, 2, 2)

'''map dada numbers'''
PLAYER_IMG_NO = 6
RED_GHOST_IMG_NO = 5
PINK_GHOST_IMG_NO = 4
GREEN_GHOST_IMG_NO = 2
ORANGE_GHOST_IMG_NO = 3
POWER_PELLET_IMG_NO = 9
DOT_IMG_NO = 8
WALLS_IMG_NO_LIST = []
for i in range(10, 24):
    WALLS_IMG_NO_LIST.append(i)
"""img path"""
'''walls'''
WALLS_IMG_PATH_DIC = {}
for i in range(10, 24):
    WALLS_IMG_PATH_DIC[i] = path.join(IMAGE_DIR, f"wall_{i}.png")
'''player'''
PLAYER_IMG_PATH_DIC = {LEFT_IMG: {}, RIGHT_IMG: {}, UP_IMG: {}, DOWN_IMG: {}}
PLAYER_IMAGE_URL = {LEFT_IMG: {}, RIGHT_IMG: {}, UP_IMG: {}, DOWN_IMG: {}}
for i in range(4):
    PLAYER_IMG_PATH_DIC[LEFT_IMG][i] = path.join(IMAGE_DIR, f"pac_man_left_{i}.png")
    PLAYER_IMG_PATH_DIC[RIGHT_IMG][i] = path.join(IMAGE_DIR, f"pac_man_right_{i}.png")
    PLAYER_IMG_PATH_DIC[UP_IMG][i] = path.join(IMAGE_DIR, f"pac_man_up_{i}.png")
    PLAYER_IMG_PATH_DIC[DOWN_IMG][i] = path.join(IMAGE_DIR, f"pac_man_down_{i}.png")
    PLAYER_IMAGE_URL[LEFT_IMG][
        i] = f"https://github.com/Jesse-Jumbo/pac-man_game/blob/feature/refactor_to_paia/asset/image/pac_man_left_{i}.png"
    PLAYER_IMAGE_URL[RIGHT_IMG][
        i] = f"https://github.com/Jesse-Jumbo/pac-man_game/blob/feature/refactor_to_paia/asset/image/pac_man_right_{i}.png"
    PLAYER_IMAGE_URL[UP_IMG][
        i] = f"https://github.com/Jesse-Jumbo/pac-man_game/blob/feature/refactor_to_paia/asset/image/pac_man_up_{i}.png"
    PLAYER_IMAGE_URL[DOWN_IMG][
        i] = f"https://github.com/Jesse-Jumbo/pac-man_game/blob/feature/refactor_to_paia/asset/image/pac_man_down_{i}.png"
'''blue'''
BLUE_GHOST_IMAGE_PATH_DIC = {DOWN_IMG: path.join(IMAGE_DIR, "blue_ghost_d.png"), LEFT_IMG: path.join(IMAGE_DIR, "blue_ghost_l.png"), RIGHT_IMG: path.join(IMAGE_DIR, "blue_ghost_r.png"),
                             UP_IMG: path.join(IMAGE_DIR, "blue_ghost_u.png")}
BLUE_GHOST_IMAGE_URL = {
    DOWN_IMG: f"https://github.com/Jesse-Jumbo/pac-man_game/blob/feature/refactor_to_paia/asset/image/blue_ghost_d.png",
    LEFT_IMG: f"https://github.com/Jesse-Jumbo/pac-man_game/blob/feature/refactor_to_paia/asset/image/blue_ghost_l.png",
    RIGHT_IMG: f"https://github.com/Jesse-Jumbo/pac-man_game/blob/feature/refactor_to_paia/asset/image/blue_ghost_r.png",
    UP_IMG: f"https://github.com/Jesse-Jumbo/pac-man_game/blob/feature/refactor_to_paia/asset/image/blue_ghost_u.png"}
'''orange'''
ORANGE_GHOST_IMAGE_PATH_DIC = {DOWN_IMG: path.join(IMAGE_DIR, "orange_ghost_d.png"), LEFT_IMG: path.join(IMAGE_DIR, "orange_ghost_l.png"),
                               RIGHT_IMG: path.join(IMAGE_DIR, "orange_ghost_r.png"), UP_IMG: path.join(IMAGE_DIR, "orange_ghost_u.png")}
'''pink'''
PINK_GHOST_IMAGE_PATH_DIC = {DOWN_IMG: path.join(IMAGE_DIR, "pink_ghost_d.png"), LEFT_IMG: path.join(IMAGE_DIR, "pink_ghost_l.png"), RIGHT_IMG: path.join(IMAGE_DIR, "pink_ghost_r.png"),
                             UP_IMG: path.join(IMAGE_DIR, "pink_ghost_u.png")}
'''red'''
RED_GHOST_IMAGE_PATH_DIC = {DOWN_IMG: path.join(IMAGE_DIR, "red_ghost_d.png"), LEFT_IMG: path.join(IMAGE_DIR, "red_ghost_l.png"), RIGHT_IMG: path.join(IMAGE_DIR, "red_ghost_r.png"),
                            UP_IMG: path.join(IMAGE_DIR, "red_ghost_u.png")}
'''green'''
GREEN_GHOST_IMAGE_PATH_DIC = {DOWN_IMG: path.join(IMAGE_DIR, "green_ghost_d.png"), LEFT_IMG: path.join(IMAGE_DIR, "green_ghost_l.png"), RIGHT_IMG: path.join(IMAGE_DIR, "green_ghost_r.png"),
                              UP_IMG: path.join(IMAGE_DIR, "green_ghost_u.png")}
'''dot'''
DOT_IMG_PATH = path.join(IMAGE_DIR, "dots.png")
POWER_PELLET_IMG_PATH = path.join(IMAGE_DIR, "power_pellet.png")

'''music'''
BGM = path.join(SOUND_DIR, 'bgm.ogg')
INVINCIBILITY_MUSIC = path.join(SOUND_DIR, 'invincibility.wav')
GHOST_SND = path.join(SOUND_DIR, 'ghost.mp3')
