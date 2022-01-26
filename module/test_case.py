import random

from games.pac_man.module.Game import Game
# from games.pac_man.module.settings import DOT_COUNT


def blue_ghost_movement(x_move, y_move):
    x_move = x_move
    y_move = y_move
    if abs(x_move) > abs(y_move):
        if x_move >= 0:
            return "r"
        else:
            return "l"
    else:
        if y_move >= 0:
            return "d"
        else:
            return "u"


def test_blue_ghost_movement():
    assert blue_ghost_movement(0, 0) == "d"
    assert blue_ghost_movement(0, 1) == "d"
    assert blue_ghost_movement(1, 0) == "r"
    assert blue_ghost_movement(1, 1) == "d"
    assert blue_ghost_movement(0, -1) == "u"
    assert blue_ghost_movement(-1, 0) == "l"
    assert blue_ghost_movement(-1, -1) == "u"
    assert blue_ghost_movement(1, 2) == "d"
    assert blue_ghost_movement(2, 1) == "r"
    assert blue_ghost_movement(-2, 1) == "l"
    assert blue_ghost_movement(1, -2) == "u"
    assert blue_ghost_movement(-1, -2) == "u"
    assert blue_ghost_movement(-2, -1) == "l"
    assert blue_ghost_movement(2, 2) == "d"
    assert blue_ghost_movement(-2, -2) == "u"
    assert blue_ghost_movement(-3, 0) == "l"


def test_create_dots():
    game = Game()
    game.create_dots()
    assert len(game.dots) == DOT_COUNT


def get_node_pos(node_pos, all_node_pos):
    if node_pos in list(all_node_pos.values()):
        return node_pos

def test_node_pos():
    game = Game()
    all_node_pos = game.node_pos
    node_pos = random.choice(list(all_node_pos.values()))
    assert node_pos == get_node_pos(node_pos, all_node_pos)
