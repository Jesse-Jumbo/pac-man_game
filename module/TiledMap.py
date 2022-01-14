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

    def render(self, game):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            for x, y, gid, in layer:
                if isinstance(layer, pytmx.TiledTileLayer) and layer.name == 'walls':
                    tile = ti(gid)
                    if tile:
                        Obstacle(game, game.walls, tile, x * TILE_SIZE , y * TILE_SIZE)
            if isinstance(layer, pytmx.TiledTileLayer) and layer.name == 'points':
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        Point(game, tile, x * TILE_SIZE, y * TILE_SIZE)
            if isinstance(layer, pytmx.TiledTileLayer) and layer.name =='red_ghost':
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        RedGhost(game, tile, x * TILE_SIZE, y * TILE_SIZE)
            if isinstance(layer, pytmx.TiledTileLayer) and layer.name =='pink_ghost':
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        PinkGhost(game, tile, x * TILE_SIZE, y * TILE_SIZE)
            if isinstance(layer, pytmx.TiledTileLayer) and layer.name =='green_ghost':
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        GreenGhost(game, tile, x * TILE_SIZE, y * TILE_SIZE)
            if isinstance(layer, pytmx.TiledTileLayer) and layer.name =='orange_ghost':
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        OrangeGhost(game, tile, x * TILE_SIZE, y * TILE_SIZE)
            if isinstance(layer, pytmx.TiledTileLayer) and layer.name =='player':
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        PacMan(game, x * TILE_SIZE, y * TILE_SIZE)
            if isinstance(layer, pytmx.TiledTileLayer) and layer.name =='dots':
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        Dot(game, tile, x * TILE_SIZE, y * TILE_SIZE)


    def make_map(self, game):
        self.render(game)