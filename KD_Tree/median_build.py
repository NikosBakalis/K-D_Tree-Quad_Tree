from collections import namedtuple

dimensions = 2
kdNode = namedtuple('kdNode', 'node leftChild rightChild')

def kdTreeBuild(points, depth = 0):
    if not points:
        return None
    axis = depth % dimensions
    points.sort(key = lambda tup: tup[axis])
    median = int(len(points) / 2)
    root = kdNode(node = points[median], leftChild = kdTreeBuild(points[:median], depth + 1), rightChild = kdTreeBuild(points[median + 1:], depth + 1))
    return root
