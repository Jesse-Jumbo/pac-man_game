import pygame

from .settings import *
import heapq
from collections import deque

vec = pygame.math.Vector2


class SquareGrid:
    def __init__(self, game, width, height):
        self.game = game
        self.width = width
        self.height = height
        walls = []
        for wall in game.walls:
            walls.append(vec(wall.pos))
        self.walls = walls
        self.connections = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]

    def in_bounds(self, node):
        return 0 <= node.x < self.width and 0 <= node.y < self.height

    def passable(self, node):
        return node not in self.walls

    def find_neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        # if (node.x + node.y) % 2:
        #     neighbors.reverse()
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors

    # def draw(self):
    #     for wall in self.walls:
    #         rect = pygame.Rect(wall * TILE_SIZE, (TILE_SIZE, TILE_SIZE))
    #         pygame.draw.rect(game.window, LIGHTGREY, rect)


class WeightedGrid(SquareGrid):
    def __init__(self, game, width, height):
        super().__init__(game, width, height)
        self.weights = {}
        for hose in game.home:
            self.weights[hose.pos] = 500

    def cost(self, from_node, to_node):
        # is go up or down or right or left
        if (vec(to_node) - vec(from_node)).length_squared() == 1:
            # + cost on key node's value
            return self.weights.get(to_node, 0) + 10

    def draw(self):
        for wall in self.walls:
            rect = pygame.Rect(wall * TILE_SIZE, (TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(self.game.window, LIGHTGREY, rect)
        for tile in self.weights:
            x, y = tile
            rect = pygame.Rect(x * TILE_SIZE + 3, y * TILE_SIZE + 3, TILE_SIZE - 3, TILE_SIZE - 3)
            pygame.draw.rect(self.game.window, FOREST, rect)


class PriorityQueue:
    def __init__(self):
        self.nodes = []

    def put(self, node, cost):
        heapq.heappush(self.nodes, (cost, node))

    def get(self):
        return heapq.heappop(self.nodes)[1]

    def empty(self):
        return len(self.nodes) == 0


def vec2int(v):
    return (int(v.x), int(v.y))


def breadth_first_search(graph, start, end):
    frontier = deque()
    frontier.append(start)
    path = {}
    path[vec2int(start)] = None
    while len(frontier) > 0:
        current = frontier.popleft()
        if current == end:
            break
        for next in graph.find_neighbors(current):
            if vec2int(start) not in path:
                frontier.append(next)
                path[vec2int(next)] = current - next
    return path


def heuristic(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y) * 10


def a_star_search(graph, start, end):
    frontier = PriorityQueue()
    frontier.put(vec2int(start), 0)
    path = {}
    cost = {}
    path[vec2int(start)] = vec(0, 0)
    cost[vec2int(start)] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for next in graph.find_neighbors(vec(current)):
            next = vec2int(next)
            next_cost = cost[current] + graph.cost(current, next)
            if next not in cost or next_cost < cost[next]:
                cost[next] = next_cost
                priority = next_cost + heuristic(end, vec(next))
                frontier.put(next, priority)
                path[next] = vec(current) - vec(next)
    return path, cost


def dijkstra_search(graph, start, end):
    frontier = PriorityQueue()
    frontier.put(vec2int(start), 0)
    path = {}
    cost = {}
    path[vec2int(start)] = None
    cost[vec2int(start)] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for next in graph.find_neighbors(vec(current)):
            next = vec2int(next)
            next_cost = cost[current] + graph.cost(current, next)
            if next not in cost or next_cost < cost[next]:
                cost[next] = next_cost
                priority = next_cost
                frontier.put(next, priority)
                path[next] = vec(current) - vec(next)
    return path, cost

# game = Game()

# g = WeightedGrid(game, GRID_WIDTH, GRID_HEIGHT)


# goal = vec(14, 8)
# start = vec(20, 0)
# path, c = a_star_search(g, goal, start)
#
# for node in path:
#     x, y = node
#
# current = start
#
# while current != goal:
#     v = path[(current.x, current.y)]
#     current = current + path[vec2int(current)]