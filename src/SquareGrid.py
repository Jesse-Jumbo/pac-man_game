import pygame

import heapq
from collections import deque

from games.pac_man.src.Obstacle import Obstacle

vec = pygame.math.Vector2


class SquareGrid:
    def __init__(self, walls: pygame.sprite.Group, width: int, height: int):
        self.width = width
        self.height = height
        self.walls = []
        for wall in walls:
            if isinstance(wall, Obstacle):
                self.walls.append(wall.node_pos)
        self.connections = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]

    def in_bounds(self, node: vec):
        return 0 <= node.x < self.width and 0 <= node.y < self.height

    def passable(self, node: vec):
        return node not in self.walls

    def find_neighbors(self, node: vec):
        neighbors = [node + connection for connection in self.connections]
        # if (node.x + node.y) % 2:
        #     neighbors.reverse()
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors


class PriorityQueue:
    def __init__(self):
        self.nodes = []

    def put(self, node: tuple):
        heapq.heappush(self.nodes, node)

    def get(self):
        return heapq.heappop(self.nodes)

    def empty(self):
        return len(self.nodes) == 0


def vec2int(v: vec):
    return (int(v.x), int(v.y))


def breadth_first_search(graph: SquareGrid, goal: vec, start: vec):
    frontier = deque()
    frontier.append(goal)
    path = {}
    path[vec2int(goal)] = None
    while len(frontier) > 0:
        current = frontier.popleft()
        if current == start:
            break
        for next in graph.find_neighbors(current):
            if vec2int(goal) not in path:
                frontier.append(next)
                path[vec2int(next)] = current - next
    return path


def a_star_search(graph: SquareGrid, goal: vec, start: vec):
    frontier = PriorityQueue()
    frontier.put(vec2int(goal))
    path = {}
    path[vec2int(goal)] = vec(0, 0)
    move_path = []

    while not frontier.empty():
        current = frontier.get()
        if current == vec2int(start):
            break
        for next in graph.find_neighbors(vec(current)):
            next = vec2int(next)
            if next not in path:
                frontier.put(next)
                path[next] = vec(current) - vec(next)
                move_path.append(path[next])
    return list(reversed(move_path))
