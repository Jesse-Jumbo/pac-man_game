from .setting import *


class Map:
    def __init__(self, filename):
        self.map_data = []
        with open(filename, 'rt') as r_f:
            for line in r_f:
                self.map_data.append(line.strip())


        self.tile_width = len(self.map_data[0])
        self.tile_height = len(self.map_data)
        self.width = self.tile_width * TILE_SIZE
        self.height = self.tile_height * TILE_SIZE