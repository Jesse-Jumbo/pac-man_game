import pygame

from module.setting import *
from module.PacMan import PacMan
from module.Dot import Dot
from module.Ghost import Ghost
from module.RedGhost import RedGhost


player = PacMan()
all_sprite.add(player)

dots = pygame.sprite.Group()
for i in range(100):
    dot = Dot()
    all_sprite.add(dot)
    dots.add(dot)

red_ghost = RedGhost(RED, 400, 200)
all_sprite.add(red_ghost)

running = True
while running:
    clock.tick(FPS)
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False

    all_sprite.update()
    all_sprite.draw(window)

    pygame.display.flip()

pygame.quit()
