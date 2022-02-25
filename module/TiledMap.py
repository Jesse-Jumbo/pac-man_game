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
    def __init__(self, filename: str):
        tm = pytmx.load_pygame(filename, pixealpha=True)
        self.width = tm.tilewidth
        self.height = tm.tileheight
        self.tmxdata = tm

    def render(self, game, object_name: str):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            for x, y, gid, in layer:
                if isinstance(layer, pytmx.TiledTileLayer) and layer.name == WALL_LAYER_NAME and object_name == WALL_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        wall = Obstacle(tile, x * TILE_SIZE, y * TILE_SIZE)
                        game.all_sprites.add(wall)
                        game.walls.add(wall)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == POINT_LAYER_NAME and object_name == POINT_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        point = Point(tile, x * TILE_SIZE, y * TILE_SIZE)
                        game.all_sprites.add(point)
                        game.points.add(point)
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
                        dot = Dot(tile, x * TILE_SIZE, y * TILE_SIZE)
                        game.all_sprites.add(dot)
                        game.dots.add(dot)

    def make_map(self, game, object_name: str):
        return self.render(game, object_name)
