import pygame
from mlgame.view.view_model import create_image_view_data

from .TiledMap import Construction


class Dot(pygame.sprite.Sprite):
    def __init__(self, construction: Construction, **kwargs):
        super().__init__()
        self.id = construction.id
        self.no = construction.no
        self.size = construction.init_size
        self.rect = pygame.Rect(construction.init_pos, construction.init_size)
        self.angle = 0
        self.image_id = "dots"

    def get_data_from_obj_to_game(self) -> dict:
        info = {"id": self.image_id
                , "x": self.rect.x
                , "y": self.rect.y
                }
        return info

    def get_obj_progress_data(self) -> dict:
        image_data = create_image_view_data(self.image_id, *self.rect.topleft,
                                            *self.size, self.angle
                                            )
        return image_data
