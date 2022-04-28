import pytmx

from games.PacMan.src.Dot import Dot
from games.PacMan.src.GreenGhost import GreenGhost
from games.PacMan.src.Obstacle import Obstacle
from games.PacMan.src.OrangeGhost import OrangeGhost
from games.PacMan.src.PinkGhost import PinkGhost
from games.PacMan.src.Player import Player
from games.PacMan.src.PowerPellet import PowerPellet
from games.PacMan.src.RedGhost import RedGhost
from .env import *


class PacManMap:
    def __init__(self, filename: str):
        tm = pytmx.load_pygame(filename, pixealpha=True)
        self.width = tm.tilewidth
        self.height = tm.tileheight
        self.tmxdata = tm
        self.walls = []
        self.dots = []
        self.power_pellets = []
        self.wall_no = 0
        # TODO refactor to clean code
        self.object_dic = {}
        # TODO just add ghosts
        self.red_ghost = pygame.sprite.Sprite()
        self.pink_ghost = pygame.sprite.Sprite()
        self.green_ghost = pygame.sprite.Sprite()
        self.orange_ghost = pygame.sprite.Sprite()
        self.player = pygame.sprite.Sprite()

    def render(self):
        for layer in self.tmxdata.visible_layers:
            # x: total 32, y: total 24, gid: tiled gid map number
            # x橫排 32格，y直排 24格，gid 圖塊在地圖上的編號
            for x, y, gid, in layer:
                if isinstance(layer, pytmx.TiledTileLayer):
                    if gid != 0:  # 0代表空格，無圖塊
                        if layer.parent.tiledgidmap[gid] in WALLS_NO_IMG_DIC:
                            self.wall_no += 1
                            wall = Obstacle(self.wall_no, layer.parent.tiledgidmap[gid],
                                            x * TILE_X_SIZE, y * TILE_Y_SIZE)
                            self.walls.append(wall)
                        elif layer.parent.tiledgidmap[gid] == POWER_PELLET_IMG_NO:
                            power_pellet = PowerPellet(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                            self.power_pellets.append(power_pellet)
                        elif layer.parent.tiledgidmap[gid] == DOT_IMG_NO:
                            dot = Dot(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                            self.dots.append(dot)
                        elif layer.parent.tiledgidmap[gid] == RED_GHOST_IMG_NO:
                            self.red_ghost = RedGhost(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                        elif layer.parent.tiledgidmap[gid] == PINK_GHOST_IMG_NO:
                            self.pink_ghost = PinkGhost(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                        elif layer.parent.tiledgidmap[gid] == GREEN_GHOST_IMG_NO:
                            self.green_ghost = GreenGhost(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                        elif layer.parent.tiledgidmap[gid] == ORANGE_GHOST_IMG_NO:
                            self.orange_ghost = OrangeGhost(x * TILE_X_SIZE, y * TILE_Y_SIZE)
                        elif layer.parent.tiledgidmap[gid] in PLAYER_IMG_NO_LIST:
                            self.player = Player(x * TILE_X_SIZE, y * TILE_Y_SIZE)

    def make_map(self):
        return self.render()
