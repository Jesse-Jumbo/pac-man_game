import pygame
from os import path

'''width and height'''
WIDTH = 640
HEIGHT = 480

'''environment data'''
FPS = 60
MAP_NAME = "map05.tmx"
'''color'''
BLACK = "#000000"
WHITE = "#ffffff"
RED = "#ff0000"
YELLOW = "#ffff00"
GREEN = "#00ff00"
GREY = "#8c8c8c"
BLUE = "#0000ff"
LIGHT_BLUE = "##21A1F1"
# TODO color name might be str
CYAN_BLUE = (0, 255, 255)
PINK = (255, 0, 255)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
BROWN = (100, 55, 5)
FOREST = (34, 57, 10)
MAGENTA = (255, 0, 255)
MEDGRAY = (75, 75, 75)

'''command'''
LEFT_cmd = "MOVE_LEFT"
RIGHT_cmd = "MOVE_RIGHT"
UP_cmd = "MOVE_UP"
DOWN_cmd = "MOVE_DOWN"

'''data path'''
GAME_DIR = path.dirname(__file__)
IMAGE_DIR = path.join(GAME_DIR, "../asset/image")
SOUND_DIR = path.join(GAME_DIR, 'sound')
MAP_DIR = path.join(GAME_DIR, '..', 'maps')
'''Layers'''
WALL_LAYER = 1
ITEMS_LAYER = 1
DOT_LAYER = 2
POINT_LAYER = 2
PLAYER_LAYER = 3
GHOST_LAYER = 3
EFFECTS_LAYER = 4
NODE_LAYER = 4

'''BG View'''
TITLE = "Pac-Man!"
BG_COLOR = DARKGREY
TILE_X_SIZE = 20
TILE_Y_SIZE = 20
TILE_SIZE = 20
GRID_WIDTH = WIDTH / TILE_X_SIZE
GRID_HEIGHT = HEIGHT / TILE_Y_SIZE
TITLE_SIZE = 100

'''window pos'''
WIDTH_CENTER = WIDTH / 2
HEIGHT_CENTER = HEIGHT / 2

'''object size'''
ALL_OBJECT_SIZE = pygame.Rect(0, 0, 20, 20)

"""all setting"""
DOWN_IMG = 'down'
RIGHT_IMG = 'right'
UP_IMG = 'up'
LEFT_IMG = 'left'

"""map setting"""
WALL_LAYER_NAME = 'walls'
POINT_LAYER_NAME = 'points'
RED_GHOST_LAYER_NAME = 'red_ghost'
PINK_GHOST_LAYER_NAME = 'pink_ghost'
GREEN_GHOST_LAYER_NAME = 'green_ghost'
ORANGE_GHOST_LAYER_NAME = 'orange_ghost'
PLAYER_LAYER_NAME = 'player'
DOTS_LAYER_NAME = 'dots'

"""collide setting"""
WITH_GHOST = 'ghost'
WITH_PLAYER = 'player'
DOT_SCORE = 10
POINT_SCORE = 50
BLUE_GHOST_SCORE = 200
CHERRY_SCORE = 500

'''player setting'''
PLAYER_SPEED = 2.0
PLAYRE_HIT_RECT = pygame.Rect(0, 0, 18, 18)

'''ghost setting'''
GHOST_HIT_RECT = pygame.Rect(0, 0, 18, 18)
GHOST_SPEED = 2.0
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

'''red'''
RED_GO = -1
'''pink'''
PINK_GO = -15
'''green'''
GREEN_GO = -30
'''orange'''
ORANGE_GO = -45

'''wall setting'''
WALL_IMG = "wall.png"

'''dot setting'''
DOT_HIT_RECT = pygame.Rect(0, 0, 5, 5)

'''point setting'''
POINT_HIT_RECT = pygame.Rect(0, 0, 8, 8)

'''node setting'''
NODE_HIT_RECT = pygame.Rect(0, 0, 2, 2)

"""img"""
'''player'''
PLAYER_IMG_LIST = ["pac_man_cc.png", "pac_man_c.png", "pac_man_o.png", "pac_man_oo.png"]
'''blue'''
blue_ghost_image_dic = {DOWN_IMG: "blue_ghost_d.png", LEFT_IMG: "blue_ghost_l.png", RIGHT_IMG: "blue_ghost_r.png", UP_IMG: "blue_ghost_u.png"}
'''orange'''
orange_ghost_image_dic = {DOWN_IMG: "orange_ghost_d.png", LEFT_IMG: "orange_ghost_l.png", RIGHT_IMG: "orange_ghost_r.png", UP_IMG: "orange_ghost_u.png"}
'''pink'''
pink_ghost_image_dic = {DOWN_IMG: "pink_ghost_d.png", LEFT_IMG: "pink_ghost_l.png", RIGHT_IMG: "pink_ghost_r.png", UP_IMG: "pink_ghost_u.png"}
'''red'''
red_ghost_image_dic = {DOWN_IMG: "red_ghost_d.png", LEFT_IMG: "red_ghost_l.png", RIGHT_IMG: "red_ghost_r.png", UP_IMG: "red_ghost_u.png"}
'''green'''
green_ghost_image_dic = {DOWN_IMG: "green_ghost_d.png", LEFT_IMG: "green_ghost_l.png", RIGHT_IMG: "green_ghost_r.png", UP_IMG: "green_ghost_u.png"}
'''dot'''
DOT_IMG = "dot.png"
POINT_IMG = "point.png"

'''music'''
BGM = 'pacman background music.ogg'
MENU_SND = 'MenuTheme.wav'
ALL_GHOST_GO_OUT = 'Destractor.mp3'
# TODO refactor URL
'''image url'''
# COMPUTER_CAR_URL = "https://raw.githubusercontent.com/yen900611/RacingCar/master/asset/image/computer_car.png"
# USER_CAR_URL = ["https://github.com/yen900611/RacingCar/blob/master/asset/image/car1.png?raw=true",
#                 "https://github.com/yen900611/RacingCar/blob/master/asset/image/car2.png?raw=true",
#                 "https://github.com/yen900611/RacingCar/blob/master/asset/image/car3.png?raw=true",
#                 "https://github.com/yen900611/RacingCar/blob/master/asset/image/car4.png?raw=true"]
# BACKGROUND_URL = "https://github.com/yen900611/RacingCar/blob/master/asset/image/ground0.jpg?raw=true"
# INFO_COIN_URL = "https://github.com/yen900611/RacingCar/blob/master/asset/image/info_coin.png?raw=true"
# INFO_KM_URL = "https://github.com/yen900611/RacingCar/blob/master/asset/image/info_km.png?raw=true"
# FINISH_URL = "https://github.com/yen900611/RacingCar/blob/master/asset/image/finish.png?raw=true"
# START_URL = "https://github.com/yen900611/RacingCar/blob/master/asset/image/start.png?raw=true"
# COIN_URL = "https://github.com/yen900611/RacingCar/blob/master/asset/image/logo.png?raw=true"

