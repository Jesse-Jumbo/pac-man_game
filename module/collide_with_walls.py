from .Game import *

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.rect.width / 2.0
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + sprite.rect.width / 2.0
            sprite.vel.x = 0
            sprite.rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.rect.height / 2.0
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.rect.height / 2.0
            sprite.vel.y = 0
            sprite.rect.centery = sprite.pos.y
