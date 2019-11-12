import random
from collections import namedtuple
import matplotlib.pyplot as plt
import matplotlib.patches as patches

print("1")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


print("2")


''' 
class Node:
    def __init__(self, x0, y0, w, h, points):
        self.x0 = x0
        self.y0 = y0
        self.width = w
        self.height = h
        self.points = points
        self.children = []

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_points(self):
        return self.points
'''

Node = namedtuple('Node', 'topLeft topRight bottomLeft bottomRight w h points')


print("3")


class QuadTree:
    def __init__(self, k, n):
        self.threshold = k
        self.points = [(7, 3), (9, 1), (1, 8), (8, 2), (2, 5), (7, 2)]
        # self.points = [Point(random.uniform(0, 10), random.uniform(0, 10)) for x in range(n)]
        # input = [(7, 3), (9, 1), (1, 8), (8, 2), (2, 5), (7, 2)]

#    def point_insertion(self, x, y):
#        self.points.append(Point(x, y))

#    def get_points(self):
#        return self.points

    def subdivide(self):
#        dimension = 2
        det = 0
#        axis = det % dimension
#        self.points.sort(key=lambda tup: tup[axis])
#        median = round(len(self.points) / 2)
#        root = self.points[median]
#        self.points.remove(root)
        self.points.sort(key=lambda tup: tup[0])
        w = (self.points[-1][0] - self.points[0][0]) / 2
        self.points.sort(key=lambda tup: tup[1])
        h = (self.points[-1][1] - self.points[0][1]) / 2
        root = Node(None, None, None, None, w, h, self.points)
        recursive_subdivide(root, self.threshold, det)
        return root


'''
    def graph(self):
        fig = plt.figure(figsize=(12, 8))
        plt.title("Quadtree")
        ax = fig.add_subplot(111)
        c = find_children(self.root)
        print("Number of segments: %d" % len(c))
        areas = set()
        for el in c:
            areas.add(el.width * el.height)
        print("Minimum segment area: %.3f units" % min(areas))
        for n in c:
            ax.add_patch(patches.Rectangle((n.x0, n.y0), n.width, n.height, fill=False))
        x = [point.x for point in self.points]
        y = [point.y for point in self.points]
        plt.plot(x, y, 'ro')
        plt.show()
        return
'''

print("4")


def recursive_subdivide(node, k, rdet):
    if len(node.points) <= k:
        return None

    w_ = float(node.w / 2)
    h_ = float(node.h / 2)

    p = contains(node.w, node.h, w_, h_, node.points)
    bottomLeftChild = Node(None, None, None, None, w_, h_, p)

    p = contains(node.w, node.h + h_, w_, h_, node.points)
    topLeftChild = Node(None, None, None, None, w_, h_, p)

    p = contains(node.w + w_, node.h, w_, h_, node.points)
    bottomRightChild = Node(None, None, None, None, w_, h_, p)

    p = contains(node.w + w_, node.h + w_, w_, h_, node.points)
    topRightChild = Node(None, None, None, None, w_, h_, p)

    node = Node(topLeftChild, topRightChild, bottomLeftChild, bottomRightChild, node.w, node.h, p)

    recursive_subdivide(node.bottomLeft, k, rdet)
    recursive_subdivide(node.topLeft, k, rdet)
    recursive_subdivide(node.bottomRight, k, rdet)
    recursive_subdivide(node.topRight, k, rdet)

    # node.children = [x1, x2, x3, x4]

    rdet = rdet + 1


print("5")


def contains(x, y, w, h, points):
    pts = []
    for point in points:
        if x <= 2 <= x + w and y <= 5 <= y + h:
            pts.append(point)
            print(pts)
    return pts


def find_children(node):
    if not node.children:
        return [node]
    else:
        children = []
        for child in node.children:
            children += (find_children(child))
    return children


print("6")

qt = QuadTree
qt.__init__(qt, 2, 2)
root = qt.subdivide(qt)
print(root)
# qt.graph()
