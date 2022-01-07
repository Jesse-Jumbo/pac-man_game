# Pac-Man Game

import pygame
import random

from os import path



'''window'''
WIDTH = 1024
HEIGHT = 768
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

'''Layers'''
WALL_LAYER = 1
ITEMS_LAYER = 1
DOT_LAYER = 2
POINT_LAYER = 2
PLAYER_LAYER = 2
GHOST_LAYER = 3
EFFECTS_LAYER = 4

'''BG View'''
TITLE = "Pac-Man!"
BG_COLOR = DARKGREY
TILE_SIZE = 32
GRID_WIDTH = WIDTH/TILE_SIZE
GRID_HEIGHT = HEIGHT/TILE_SIZE

'''player setting'''
PLAYER_SPEED = 100.0
# PLAYER_ROT_SPEED = 250.0
PLAYRE_HIT_RECT = pygame.Rect(0, 0, 28, 28)

'''ghost setting'''
GHOST_HIT_RECT = pygame.Rect(0, 0, 28, 28)
AVOID_RADIUS = 50
GHOST_SPEED = 90.0
'''wall setting'''
WALL_IMG = "wall.png"
'''dot setting'''
dot_amount = range(100)

'''img'''
'''player'''
# PLAYER_IMG = "pac.png"
PLAYER_IMG_LIST = ["pac_man_cc.png", "pac_man_c.png", "pac_man_o.png", "pac_man_oo.png"]
'''blue'''
blue_ghost_image_dic = {"down": "blue_ghost_d.png", "left": "blue_ghost_l.png", "right": "blue_ghost_r.png", "up": "blue_ghost_u.png"}
'''orange'''
orange_ghost_image_dic = {"down": "orange_ghost_d.png", "left": "orange_ghost_l.png", "right": "orange_ghost_r.png", "up": "orange_ghost_u.png"}
'''pink'''
pink_ghost_image_dic = {"down": "pink_ghost_d.png", "left": "pink_ghost_l.png", "right": "pink_ghost_r.png", "up": "pink_ghost_u.png"}
'''red'''
red_ghost_image_dic = {"down": "red_ghost_d.png", "left": "red_ghost_l.png", "right": "red_ghost_r.png", "up": "red_ghost_u.png"}
'''green'''
green_ghost_image_dic = {"down": "green_ghost_d.png", "left": "green_ghost_l.png", "right": "green_ghost_r.png", "up": "green_ghost_u.png"}
'''dot'''
DOT_IMG = "dot.png"
POINT_IMG = "point.png"

'''snd'''
BGM = 'pacman background music.ogg'
MENU_SND = 'MenuTheme.wav'
ALL_GHOST_GO_OUT = 'Destractor.mp3'