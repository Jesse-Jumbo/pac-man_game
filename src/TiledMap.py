import pytmx

from games.pac_man.src.GreenGhost import GreenGhost
from games.pac_man.src.OrangeGhost import OrangeGhost
from games.pac_man.src.PinkGhost import PinkGhost
from games.pac_man.src.RedGhost import RedGhost
from .env import *
from games.pac_man.src.Dot import Dot
from games.pac_man.src.Obstacle import Obstacle
from games.pac_man.src.Player import Player
from games.pac_man.src.Point import Point


class TiledMap:
    def __init__(self, filename: str):
        tm = pytmx.load_pygame(filename, pixealpha=True)
        self.width = tm.tilewidth
        self.height = tm.tileheight
        self.tmxdata = tm
        self.walls = []
        self.dots = []
        self.points = []

    def render(self, object_name: str):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            for x, y, gid, in layer:
                if isinstance(layer, pytmx.TiledTileLayer) and layer.name == WALL_LAYER_NAME and object_name == WALL_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        wall = Obstacle(tile, x * TILE_X_SIZE, y * TILE_Y_SIZE)
                        self.walls.append(wall)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == POINT_LAYER_NAME and object_name == POINT_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        point = Point(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                        self.points.append(point)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == RED_GHOST_LAYER_NAME and object_name == RED_GHOST_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        return RedGhost(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == PINK_GHOST_LAYER_NAME and object_name == PINK_GHOST_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        return PinkGhost(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == GREEN_GHOST_LAYER_NAME and object_name == GREEN_GHOST_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        return GreenGhost(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == ORANGE_GHOST_LAYER_NAME and object_name == ORANGE_GHOST_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        return OrangeGhost(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == PLAYER_LAYER_NAME and object_name == PLAYER_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        return Player(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == DOTS_LAYER_NAME and object_name == DOTS_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        dot = Dot(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                        self.dots.append(dot)

    def make_map(self, object_name: str):
        return self.render(object_name)
