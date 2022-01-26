# Pac-Man Game

import pygame
import random

from os import path



'''window'''
WIDTH = 640
HEIGHT = 480
FPS = 64

'''color'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN_BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
BROWN = (100, 55, 5)
FOREST = (34, 57, 10)
MAGENTA = (255, 0, 255)
MEDGRAY = (75, 75, 75)

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
TILE_SIZE = 20
GRID_WIDTH = WIDTH/TILE_SIZE
GRID_HEIGHT = HEIGHT/TILE_SIZE

"""map setting"""
WALL_LAYER_NAME = 'walls'
POINT_LAYER_NAME = 'points'
RED_GHOST_LAYER_NAME = 'red_ghost'
PINK_GHOST_LAYER_NAME = 'pink_ghost'
GREEN_GHOST_LAYER_NAME = 'green_ghost'
ORANGE_GHOST_LAYER_NAME = 'orange_ghost'
PLAYER_LAYER_NAME = 'player'
DOTS_LAYER_NAME = 'dots'
HOME_LAYER_NAME = 'home'

"""collide setting"""
WITH_GHOST = 'ghost'
WITH_PLAYER = 'player'
DOT_SCORE = 10
POINT_SCORE = 50
BLUE_GHOST_SCORE = 200
CHERRY_SCORE = 500

'''player setting'''
PLAYER_SPEED = 200.0
PLAYRE_HIT_RECT = pygame.Rect(0, 0, 18, 18)

'''ghost setting'''
GHOST_HIT_RECT = pygame.Rect(0, 0, 18, 18)
GHOST_SPEED = 90.0
SPEED_SLOW = -30
RED_MODULE = 'red'
PINK_MODULE = 'pink'
GREEN_MODULE = 'green'
ORANGE_MODULE = 'orange'
BLUE_IMG = 'blue_ghost_img'
RED_IMG = 'red_ghost_img'
PINK_IMG = 'pink_ghost_img'
GREEN_IMG = 'green_ghost_img'
ORANGE_IMG = 'orange_ghost_img'
BLUE_LIMIT = 10000

"""all setting"""
DOWN_IMG = 'down'
RIGHT_IMG = 'right'
UP_IMG = 'up'
LEFT_IMG = 'left'
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
node_width = 50
node_height = 50

'''img'''
'''player'''
# PLAYER_IMG = "pac.png"
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