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
                if isinstance(layer, pytmx.TiledTileLayer) and layer.name == 'walls' and object_name == 'walls':
                    tile = ti(gid)
                    if tile:
                        Obstacle(game, game.walls, tile, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == 'points' and object_name == 'points':
                    tile = ti(gid)
                    if tile:
                        Point(game, tile, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == 'red_ghost' and object_name == 'red_ghost':
                    tile = ti(gid)
                    if tile:
                        RedGhost(game, tile, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == 'pink_ghost' and object_name == 'pink_ghost':
                    tile = ti(gid)
                    if tile:
                        PinkGhost(game, tile, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == 'green_ghost' and object_name == 'green_ghost':
                    tile = ti(gid)
                    if tile:
                        GreenGhost(game, tile, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == 'orange_ghost' and object_name == 'orange_ghost':
                    tile = ti(gid)
                    if tile:
                        OrangeGhost(game, tile, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == 'player' and object_name == 'player':
                    tile = ti(gid)
                    if tile:
                        PacMan(game, x * TILE_SIZE, y * TILE_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == 'dots' and object_name == 'dots':
                    tile = ti(gid)
                    if tile:
                        Dot(game, tile, x * TILE_SIZE, y * TILE_SIZE)


    def make_map(self, game, object_name):
        self.render(game, object_name)