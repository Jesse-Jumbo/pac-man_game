import pygame.sprite

from .settings import *
from games.pac_man.module.collide_hit_rect import collide_hit_rect


def collide_with_nodes(sprite: pygame.sprite, group: pygame.sprite.Group, dir: str):
    # TODO abstraction refactor if

    if dir == 'node':
        for node in group:
            if node.pos.x - 1 <= sprite.pos.x <= node.pos.x + 1:
                sprite.node_pos.x = node.pos.x / TILE_SIZE
            if node.pos.y - 1 <= sprite.pos.y <= node.pos.y + 1:
                sprite.node_pos.y = node.pos.y / TILE_SIZE