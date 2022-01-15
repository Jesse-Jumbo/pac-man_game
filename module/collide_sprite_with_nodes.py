import pygame

from games.pac_man.module.collide_hit_rect import collide_hit_rect


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