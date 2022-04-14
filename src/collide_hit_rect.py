import pygame.sprite

from .Dot import Dot
from .Ghost import Ghost
from .Player import Player
from .env import *


def collide_hit_rect(one: pygame.sprite, two: pygame.sprite):
    return one.hit_rect.colliderect(two.hit_rect)


# TODO refactor collide
# collide player with ghosts
def collide_player_with_ghosts(sprite: Player, group: pygame.sprite.Group):
    hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
    if hits:
        ghost = hits[0]
        if isinstance(ghost, Ghost):
            if ghost.is_blue:
                sprite.blue_ghosts_score += BLUE_GHOST_SCORE
                sprite.ate_blue_ghosts_times += 1
                sprite.score += BLUE_GHOST_SCORE
                ghost.pos.xy = ghost.ghost_origin_pos
                ghost.ghost_no = ghost.origin_no
                ghost.is_blue = False
            else:
                sprite.state = False


# collide sprite with nodes
def collide_with_nodes(sprite: pygame.sprite, group: pygame.sprite.Group, dir=""):
    for node in group:
        if node.pos.x - 2 <= sprite.pos.x <= node.pos.x + 2:
            sprite.node_pos.x = node.pos.x / TILE_SIZE
        if node.pos.y - 2 <= sprite.pos.y <= node.pos.y + 2:
            sprite.node_pos.y = node.pos.y / TILE_SIZE
    if dir == "ghost":
        pass
        # sprite.search()


# collide sprite with walls
def collide_with_walls(sprite: pygame.sprite, group: pygame.sprite.Group):
    hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
    if hits:
        sprite.collide_with_walls()


def collide_with_dots(sprite: Player, group: pygame.sprite.Group):
    hits = pygame.sprite.spritecollide(sprite, group, True, collide_hit_rect)
    for hit in hits:
        sprite.collide_with_dots()

