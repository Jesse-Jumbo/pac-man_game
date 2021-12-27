import random


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
