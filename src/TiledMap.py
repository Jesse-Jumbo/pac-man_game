import pytmx

from games.PacMan.src.GreenGhost import GreenGhost
from games.PacMan.src.OrangeGhost import OrangeGhost
from games.PacMan.src.PinkGhost import PinkGhost
from games.PacMan.src.RedGhost import RedGhost
from .env import *
from games.PacMan.src.Dot import Dot
from games.PacMan.src.Obstacle import Obstacle
from games.PacMan.src.Player import Player
from games.PacMan.src.PowerPellet import PowerPellet


def find_img_index(img_list: list, c: int):
    for i in range(c, len(img_list)):
        if img_list[i] != 0:
            return img_list[i], i
        elif img_list[i] == 0 and i == len(img_list) - 1:
            return 0, 0

def create_wall():
    pass
class TiledMap:
    def __init__(self, filename: str):
        tm = pytmx.load_pygame(filename, pixealpha=True)
        self.width = tm.tilewidth
        self.height = tm.tileheight
        self.tmxdata = tm
        self.walls = []
        self.dots = []
        self.power_pellets = []
        self.wall_no = 0
        self.c = 0
        self.object_dic = {}

    # TODO refactor load map mean, remember map_07.tmx
    # def render(self):
    #     # ti = self.tmxdata.get_tile_image_by_gid
    #     for layer in self.tmxdata.visible_layers:
    #         print(*layer)
    #         for x, y, gid, in layer:
    #             if isinstance(layer, pytmx.TiledTileLayer):
    #                 # tile = ti(gid)
    #                 if gid in WALLS_NO_IMG_DIC:
    #                     self.wall_no += 1
    #                     wall = Obstacle(self.wall_no, )

    def render(self, object_name: str):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            for x, y, gid, in layer:
                if isinstance(layer, pytmx.TiledTileLayer) and layer.name == WALL_LAYER_NAME and object_name == WALL_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        self.wall_no += 1
                        wall_img_index = layer.data[y][x]
                        img_no = str(layer.parent.tiledgidmap[wall_img_index])
                        wall = Obstacle(self.wall_no, img_no, x * TILE_X_SIZE, y * TILE_Y_SIZE)
                        self.walls.append(wall)

                elif isinstance(layer, pytmx.TiledTileLayer) and layer.name == POWER_PELLET_LAYER_NAME and object_name == POWER_PELLET_LAYER_NAME:
                    tile = ti(gid)
                    if tile:
                        power_pellet = PowerPellet(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                        self.power_pellets.append(power_pellet)
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

    # def make_map(self):
    #     return self.render()
#