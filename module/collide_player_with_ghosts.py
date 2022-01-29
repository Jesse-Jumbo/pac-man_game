import pygame
from .settings import *
from games.pac_man.module.collide_hit_rect import collide_hit_rect


def collide_player_with_ghosts(sprite: pygame.sprite, group: pygame.sprite.Group, dir: str):
    # TODO abstraction refactor if

    if dir == WITH_GHOST:
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if not hits[0].is_blue:
                sprite.game.playing = False
                sprite.game.show_go_screen()
            else:
                sprite.score += BLUE_GHOST_SCORE
                hits[0].pos.xy = hits[0].ghost_origin_pos
                hits[0].is_blue = False
