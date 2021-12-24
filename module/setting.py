# Pac-Man Game

import pygame
import random

WIDTH = 800
HEIGHT = 400
FPS = 60

BLACK = (0, 0, 0)
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

all_sprite = pygame.sprite.Group()
window.fill(BLACK)