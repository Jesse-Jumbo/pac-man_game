import random

from .env import *
from mlgame.gamedev.game_interface import GameStatus


def collide_hit_rect(one: pygame.sprite, two: pygame.sprite):
    return one.hit_rect.colliderect(two.hit_rect)


# collide player with ghosts
def collide_player_with_ghosts(sprite: pygame.sprite, group: pygame.sprite.Group):

    hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
    if hits:
        if not hits[0].is_blue:
            sprite.state = False
            sprite.status = GameStatus.GAME_OVER
        else:
            sprite.score += BLUE_GHOST_SCORE
            hits[0].pos.xy = hits[0].ghost_origin_pos
            hits[0].ghost_no = hits[0].origin_no
            hits[0].is_blue = False


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
def collide_with_walls(sprite: pygame.sprite, group: pygame.sprite.Group, dir: str, ghost=False):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            elif hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x

            if ghost:
                sprite.move_cmd = random.choice([UP_cmd, DOWN_cmd])
    elif dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            elif hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

            if ghost:
                sprite.move_cmd = random.choice([LEFT_cmd, RIGHT_cmd])

