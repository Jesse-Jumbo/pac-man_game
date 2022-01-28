import random

from games.pac_man.module.SquareGrid import *


# Test SquareGrid
def test_a_star_search():
    """
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1),g(1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2),                         (4, 2),
    (0, 3), (1, 3), (2, 3),s(3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    """
    walls = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (2, 1), (3, 1), (4, 1), (0, 2), (4, 2), (0, 3), (1, 3), (2, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),]
    all_walls = []
    for wall in walls:
        all_walls.append(vec(wall))
    graph = SquareGrid(all_walls, 5, 5)
    all_path = a_star_search(graph, vec(1, 1), vec(3, 3))
    assert all_path == [vec(0, -1), vec(-1, 0), vec(-1, 0), vec(0, -1)]


#