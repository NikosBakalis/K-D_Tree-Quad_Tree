import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

print("1")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


print("2")


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


print("3")


class QuadTree:
    def __init__(self, k, n):
        self.threshold = k
        self.points = []
        # self.points = [Point(random.uniform(0, 10), random.uniform(0, 10)) for x in range(n)]
        input = [(7, 3), (9, 1), (1, 8), (8, 2), (2, 5), (7, 2)]
        for tu in input:
            self.point_insertion(self,tu[0],tu[1])

    def point_insertion(self, x, y):
        self.points.append(Point(x, y))

    def get_points(self):
        return self.points

    def subdivide(self):
        dimension = 2
        det = 0
        axis = det % dimension
        if axis == 0:
            self.points.sort(key=lambda tup: tup.x)
        if axis == 1:
            self.points.sort(key=lambda tup: tup.y)
        median = round(len(self.points) / 2)
        root = self.points[median]
        self.points.remove(root)
        node = Node
        self.points.sort(key=lambda tup: tup.x)
        w = (self.points[-1].x - self.points[0].x) / 2
        self.points.sort(key=lambda tup: tup.y)
        h = (self.points[-1].y - self.points[0].y) / 2
        node.__init__(Node, root.x, root.y, w, h, self.points)
        recursive_subdivide(node, self.threshold, det)

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

print("4")


def recursive_subdivide(node, k, rdet):
    if len(node.points) <= k:
        return

    w_ = float(node.width / 2)
    h_ = float(node.height / 2)

    p = contains(node.x0, node.y0, w_, h_, node.points)
    x1 = Node(node.x0, node.y0, w_, h_, p)
    recursive_subdivide(x1, k, rdet)

    p = contains(node.x0, node.y0 + h_, w_, h_, node.points)
    x2 = Node(node.x0, node.y0 + h_, w_, h_, p)
    recursive_subdivide(x2, k, rdet)

    p = contains(node.x0 + w_, node.y0, w_, h_, node.points)
    x3 = Node(node.x0 + w_, node.y0, w_, h_, p)
    recursive_subdivide(x3, k, rdet)

    p = contains(node.x0 + w_, node.y0 + w_, w_, h_, node.points)
    x4 = Node(node.x0 + w_, node.y0 + h_, w_, h_, p)
    recursive_subdivide(x4, k, rdet)

    node.children = [x1, x2, x3, x4]

    rdet = rdet + 1


print("5")


def contains(x, y, w, h, points):
    pts = []
    for point in points:
        if point.x >= x and point.x <= x + w and point.y >= y and point.y <= y + h:
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
qt.subdivide(qt)
qt.graph()
