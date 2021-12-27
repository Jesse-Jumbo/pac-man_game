import pygame

from module.setting import *
from module.PacMan import PacMan
from module.Dot import Dot
from module.RedGhost import RedGhost
from module.GreenGhost import GreenGhost
from module.PinkGhost import PinkGhost
from module.OrangeGhost import OrangeGhost
from module.draw_score import draw_score


player = PacMan()
all_sprites.add(player)

dots = pygame.sprite.Group()
for i in range(100):
    dot = Dot()
    all_sprites.add(dot)
    dots.add(dot)

ghosts = pygame.sprite.Group()

red_ghost = RedGhost(390, 182.5)
all_sprites.add(red_ghost)
ghosts.add(red_ghost)

green_ghost = GreenGhost(370, 217.5)
all_sprites.add(green_ghost)
ghosts.add(green_ghost)

pink_ghost = PinkGhost(390, 217.5)
all_sprites.add(pink_ghost)
ghosts.add(pink_ghost)

orange_ghost = OrangeGhost(410, 217.5)
all_sprites.add(orange_ghost)
ghosts.add(orange_ghost)

score = 0

running = True
while running:
    clock.tick(FPS)
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False


    hits = pygame.sprite.spritecollide(player, ghosts, False)
    for hit in hits:
        running = False

    hits = pygame.sprite.spritecollide(player, dots, True)
    for hit in hits:
        score += 10

    all_sprites.update()

    window.fill(BLACK)
    all_sprites.draw(window)
    draw_score(window, str(score), 30, WIDTH / 2, 10)

    pygame.display.flip()

pygame.quit()
