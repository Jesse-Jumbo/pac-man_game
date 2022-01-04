# Pac-Man Game

import pygame
import random

from os import path



'''window'''
WIDTH = 1024
# WIDTH = 200
HEIGHT = 768
# HEIGHT = 200
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
PLAYER_IMG = "pac.png"
PLAYRE_HIT_RECT = pygame.Rect(0, 0, 28, 28)

'''ghost setting'''
GHOST_HIT_RECT = pygame.Rect(0, 0, 28, 28)
AVOID_RADIUS = 50
GHOST_SPEED = 90.0
'''blue'''
BLUE_GHOST_IMG = "blue_ghost_d.png"
BLUE_GHOST_IMG_L = "blue_ghost_l.png"
BLUE_GHOST_IMG_R = "blue_ghost_r.png"
BLUE_GHOST_IMG_U = "blue_ghost_u.png"
'''orange'''
ORANGE_GHOST_IMG = "orange_ghost_d.png"
ORANGE_GHOST_IMG_L = "orange_ghost_l.png"
ORANGE_GHOST_IMG_R = "orange_ghost_r.png"
ORANGE_GHOST_IMG_U = "orange_ghost_u.png"
'''pink'''
PINK_GHOST_IMG = "pink_ghost_d.png"
PINK_GHOST_IMG_L = "pink_ghost_l.png"
PINK_GHOST_IMG_R = "pink_ghost_r.png"
PINK_GHOST_IMG_U = "pink_ghost_u.png"
'''red'''
RED_GHOST_IMG = "red_ghost_d.png"
RED_GHOST_IMG_L = "red_ghost_l.png"
RED_GHOST_IMG_R = "red_ghost_r.png"
RED_GHOST_IMG_U = "red_ghost_u.png"
'''green'''
GREEN_GHOST_IMG = "green_ghost_d.png"
GREEN_GHOST_IMG_L = "green_ghost_l.png"
GREEN_GHOST_IMG_R = "green_ghost_r.png"
GREEN_GHOST_IMG_U = "green_ghost_u.png"
'''wall setting'''
WALL_IMG = "wall.png"