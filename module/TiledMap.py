import pygame
import pytmx

from .GreenGhost import GreenGhost
from .OrangeGhost import OrangeGhost
from .PinkGhost import PinkGhost
from .RedGhost import RedGhost
from .settings import *
from .Dot import Dot
from .Obstacle import Obstacle
from .PacMan import PacMan
from .Point import Point


class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixealpha=True)
        self.width = tm.tilewidth
        self.height = tm.tileheight
        self.tmxdata = tm

    def render(self, game, object_name):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            for x, y, gid, in layer:
                if isinstance(layer, pytmx.TiledTileLayer) and layer.name == WALL_LAYER_NAME and object_name == WALL_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        Obstacle(game, game.walls, tile, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == POINT_LAYER_NAME and object_name == POINT_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        Point(game, tile, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == RED_GHOST_LAYER_NAME and object_name == RED_GHOST_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        red_ghost = RedGhost(game, x * TILE_SIZE, y * TILE_SIZE)
                        return red_ghost
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == PINK_GHOST_LAYER_NAME and object_name == PINK_GHOST_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        return PinkGhost(game, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == GREEN_GHOST_LAYER_NAME and object_name == GREEN_GHOST_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        return GreenGhost(game, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == ORANGE_GHOST_LAYER_NAME and object_name == ORANGE_GHOST_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        return OrangeGhost(game, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == PLAYER_LAYER_NAME and object_name == PLAYER_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        player = PacMan(game, x * TILE_SIZE, y * TILE_SIZE)
                        return player
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == DOTS_LAYER_NAME and object_name == DOTS_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        Dot(game, tile, x * TILE_SIZE, y * TILE_SIZE)

    def make_map(self, game, object_name):
        return self.render(game, object_name)
