from .settings import *


class Map:
    def __init__(self, filename: str):
        self.map_data = []
        with open(filename, 'rt') as r_f:
            for line in r_f:
                self.map_data.append(line.strip())

        self.width = TILE_SIZE
        self.height = TILE_SIZE
