import pygame.font

from .setting import *


def draw_score(surf, score, size, x ,y):
    font = pygame.font.SysFont(font_name, size, bold=True)
    score_surface = font.render(score, True, WHITE)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (x, y)
    surf.blit(score_surface, score_rect)