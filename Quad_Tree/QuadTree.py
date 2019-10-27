from collections import namedtuple

nodes = [(7, 2), (6, 9), (5, 7), (4, 5), (9, 6), (1, 9), (9, 7), (5, 2), (3, 1)]


class Node(namedtuple('Node', 'x y')):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle(namedtuple('Rectangle', 'x y w h')):
    def __contains__(self, node):
        x, y = node
        if not self.x <= x <= self.x + self.w:
            return False
        if not self.y <= y <= self.y + self.h:
            return False
        return True


class QuadTree:
    def __init__(self, maxwidth, maxheight):
        self.maxwidth = maxwidth
        self.maxheight = maxheight

    def node_insertion():
        if not nodes:
            print("No nodes found")
            return None
        print("Some nodes found")


QuadTree.node_insertion()



