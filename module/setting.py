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
PLAYER_ROT_SPEED = 250.0
PLAYER_IMG = "pac.png"
# PLAYRE_HIT_RECT = pygame.Rect(0, 0, 35, 35)