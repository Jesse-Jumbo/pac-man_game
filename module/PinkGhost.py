from .collide_with_walls import collide_with_walls
from .settings import *
from .Ghost import Ghost


class PinkGhost(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = game.pink_ghost_d
        self.origin_img = game.pink_ghost_d
        self.up_img = game.pink_ghost_u
        self.right_img = game.pink_ghost_r
        self.left_image = game.pink_ghost_l

    def update(self, *args, **kwargs) -> None:
        self.pink_move()

        self.hit_rect.centerx = self.pos.x
        # collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        # collide_with_walls(self, self.game.walls, 'y')

    def pink_move(self):
        self.rot = (self.game.player.front_pos - self.pos).angle_to(pygame.math.Vector2(1, 0))
        print(self.rot)
        if -45 <= self.rot < 45:
            self.image = self.game.pink_ghost_r
            self.vel.x = GHOST_SPEED
            self.pos.x += self.vel.x * self.game.dt
        elif 45 <= self.rot < 135:
            self.image = self.game.pink_ghost_u
            self.vel.y = -GHOST_SPEED
            self.pos.y += self.vel.y * self.game.dt
        elif -135 >= self.rot or 180 >= self.rot >= 135:
            self.image = self.game.pink_ghost_l
            self.vel.x = -GHOST_SPEED
            self.pos.x += self.vel.x * self.game.dt
        else:
            self.image = self.game.pink_ghost_d
            self.vel.y = GHOST_SPEED
            self.pos.y += self.vel.y * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
