import pygame

from settings import *
from collections import deque

vec = pygame.math.Vector2


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.connections = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]

    def in_bounds(self, node):
        return 0 <= node.x < self.width and 0 <= node.y < self.height

    def passable(self, node):
        return node not in self.walls

    def find_neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors

    def draw(self, game):
        for wall in self.walls:
            rect = pygame.Rect(wall * TILE_SIZE, (TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(game.window, LIGHTGREY, rect)

def vec2int(v):
    return (int(v.x), int(v.y))

def breadth_first_search(graph, start):
    frontier = deque()
    frontier.append(start)
    path = {}
    path[vec2int(start)] = None
    while len(frontier) > 0:
        current = frontier.popleft()
        for next in graph.find_neighbors(current):
            if vec2int(start) not in path:
                frontier.append(next)
                path[vec2int(next)] = current - next
    return path

g = SquareGrid(GRID_WIDTH, GRID_HEIGHT)
start = vec(14, 8)
patg = breadth_first_search(g, start)