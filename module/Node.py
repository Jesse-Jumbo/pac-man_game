import pygame

from .settings import *


class Node(pygame.sprite.Sprite):
    def __init__(self, game, value=None, node_pos_x=None, node_pos_y=None, width=None, height=None):
        self._layer = NODE_LAYER
        self.group = game.nodes
        super().__init__(self.group)
        self.value = value
        self.node_pos = pygame.math.Vector2(node_pos_x, node_pos_y)
        self.left_child = None  # smaller
        self.right_child = None  # greater
        self.parent = None  # pointer to parent node in tree
        self.update_time = pygame.time.get_ticks()
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.node_pos.x, self.node_pos.y, self.width, self.height)


class Binary_search_tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.root = None

    def insert(self, game, value, node_pos_x=None, node_pos_y=None, width=None, height=None):
        if self.root is None:
            self.root = Node(game, value, node_pos_x, node_pos_y, width, height)
            self.rect = self.root.rect
        else:
            self._insert(game, value, self.root, node_pos_x, node_pos_y, width, height)

    def _insert(self, game, value, cur_node, node_pos_x=None, node_pos_y=None, width=None, height=None):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(game, value, node_pos_x, node_pos_y, width, height)
                cur_node.left_child.parent = cur_node  # set parent
            else:
                self._insert(game, value, cur_node.left_child, node_pos_x, node_pos_y, width, height)

        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(game, value, node_pos_x, node_pos_y, width, height)
                cur_node.right_child.parent = cur_node  # set parent
            else:
                self._insert(game, value, cur_node.right_child, node_pos_x, node_pos_y, width, height)

        # value == cur_node.value
        else:
            print("This value has existed")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)


def fill_tree(game, tree, value, node_pos_x=None, node_pos_y=None, width=None, height=None):
    tree.insert(game, value, node_pos_x, node_pos_y, width, height)
    return tree


# tree = Binary_search_tree()
# tree = fill_tree(tree, ["2222222222", "33333"], [25, 20])
#
# tree.print_tree()

# def create_two(index, length, arr):
#     if index > length:
#         return None
#
#     node = Node(arr[index])
#     node.left_child = create_two(index*2+1, length, arr)
#     node.right_child = create_two(index*2+2, length, arr)
#
#     return node
#
# def BFS(root):
#     queue = [root]
#     while queue:
#         cur = queue.pop(0)
#         # print(cur.value)
#
#         if cur.left_child:
#             queue.append(cur.left_child)
#
#         if cur.right_child:
#             queue.append(cur.right_child)
#
# arr = [1, 2, 3, 4, 5, None, None, None]
# length = len(arr) - 1
# for i in arr:
#     head = create_two(i, length, arr)
#
#     print(head.value)
#     print(head.left_child)
#     print(head.right_child)
#
# # BFS(head)
