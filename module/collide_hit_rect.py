from .settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.hit_rect)