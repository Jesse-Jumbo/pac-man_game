from .collide_hit_rect import collide_hit_rect
from .settings import *


def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y
    if dir == 'wall':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            sprite.rect.x = random.randint(0 + TILE_SIZE, WIDTH - TILE_SIZE)
            sprite.rect.y = random.randint(0 + TILE_SIZE, HEIGHT - TILE_SIZE)


def collide_with_nodes(sprite, group, dir):
    if dir == 'node':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            sprite.node_value = hits[0].value

    if dir == 'update_node':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            sprite.node_value = hits[0].value
            hits[0].update_time = pygame.time.get_ticks()

    if dir == 'target':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.node_value > sprite.game.player.node_value:
                if hits[0].parent:
                    if hits[0].parent.update_time > hits[0].right_child.update_time:
                        target_pos = hits[0].parent.node_pos
                    else:
                        target_pos = hits[0].right_child.node_pos
            elif sprite.node_value < sprite.game.player.node_value:
                target_pos = hits[0].left_child.node_pos
            else:
                target_pos = sprite.game.player.pos

            sprite.rot = (target_pos - hits[0].node_pos).angle_to(pygame.math.Vector2(1, 0))
            if -45 <= sprite.rot < 45:
                sprite.image = sprite.right_img
                sprite.vel.x = sprite.speed
                sprite.pos.x += sprite.vel.x * sprite.game.dt
            elif 45 <= sprite.rot < 135:
                sprite.image = sprite.up_img
                sprite.vel.y = -sprite.speed
                sprite.pos.y += sprite.vel.y * sprite.game.dt
            elif -135 >= sprite.rot or 180 >= sprite.rot >= 135:
                sprite.image = sprite.left_image
                sprite.vel.x = -sprite.speed
                sprite.pos.x += sprite.vel.x * sprite.game.dt
            else:
                sprite.image = sprite.origin_img
                sprite.vel.y = sprite.speed
                sprite.pos.y += sprite.vel.y * sprite.game.dt
            sprite.rect = sprite.image.get_rect()
            sprite.rect.center = sprite.pos

def ghost_collide(sprite, group, dir):
    if dir == 'ghost':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if not hits[0].is_blue:
                sprite.game.playing = False
                sprite.game.show_go_screen()

    if dir == 'player':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].is_blue:
                sprite.game.score += 200
                hits[0].pos.xy = sprite.game.red_origin_pos
                hits[0].is_blue = False
