# Pac-Man Game

import pygame
import random

from os import path


img_dir = path.join(path.dirname(__file__), '../img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 1024
HEIGHT = 768
FPS = 64

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN_BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Pac-Man!")
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))

'''font'''
font_name = pygame.font.match_font('arial')

all_sprites = pygame.sprite.Group()

"""img"""
player_img = pygame.image.load(path.join(img_dir, "pac.png")).convert_alpha()

small_dot_img = pygame.image.load(path.join(img_dir, "dot.png")).convert_alpha()
big_dot_img = pygame.image.load(path.join(img_dir, "point.png")).convert_alpha()

blue_ghost_d = pygame.image.load(path.join(img_dir, "blue_ghost_d.png")).convert_alpha()
blue_ghost_u = pygame.image.load(path.join(img_dir, "blue_ghost_u.png")).convert_alpha()
blue_ghost_r = pygame.image.load(path.join(img_dir, "blue_ghost_r.png")).convert_alpha()
blue_ghost_l = pygame.image.load(path.join(img_dir, "blue_ghost_l.png")).convert_alpha()

green_ghost_d = pygame.image.load(path.join(img_dir, "green_ghost_d.png")).convert_alpha()
green_ghost_u = pygame.image.load(path.join(img_dir, "green_ghost_u.png")).convert_alpha()
green_ghost_r = pygame.image.load(path.join(img_dir, "green_ghost_r.png")).convert_alpha()
green_ghost_l = pygame.image.load(path.join(img_dir, "green_ghost_l.png")).convert_alpha()

red_ghost_d = pygame.image.load(path.join(img_dir, "red_ghost_d.png")).convert_alpha()
red_ghost_u = pygame.image.load(path.join(img_dir, "red_ghost_u.png")).convert_alpha()
red_ghost_r = pygame.image.load(path.join(img_dir, "red_ghost_r.png")).convert_alpha()
red_ghost_l = pygame.image.load(path.join(img_dir, "red_ghost_l.png")).convert_alpha()

pink_ghost_u = pygame.image.load(path.join(img_dir, "pink_ghost_u.png")).convert_alpha()
pink_ghost_d = pygame.image.load(path.join(img_dir, "pink_ghost_d.png")).convert_alpha()
pink_ghost_r = pygame.image.load(path.join(img_dir, "pink_ghost_r.png")).convert_alpha()
pink_ghost_l = pygame.image.load(path.join(img_dir, "pink_ghost_l.png")).convert_alpha()

orange_ghost_u = pygame.image.load(path.join(img_dir, "orange_ghost_u.png")).convert_alpha()
orange_ghost_d = pygame.image.load(path.join(img_dir, "orange_ghost_d.png")).convert_alpha()
orange_ghost_r = pygame.image.load(path.join(img_dir, "orange_ghost_r.png")).convert_alpha()
orange_ghost_l = pygame.image.load(path.join(img_dir, "orange_ghost_l.png")).convert_alpha()
