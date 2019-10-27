from collections import namedtuple

points = [(7,2), (5,4), (9,6), (4,7), (8,1), (2,3)]
dimensions = 2
kdNode = namedtuple('kdNode', 'node leftChild rightChild')

def kdTreeBuild(points, depth = 0):
    if not points:
        return None
    axis = depth % dimensions
    points.sort(key = lambda tup: tup[axis])
    median = round(len(points) / 2)
    root = kdNode(points[median], kdTreeBuild(points[:median],depth + 1), kdTreeBuild(points[median + 1:], depth + 1))
    return root

root = kdTreeBuild(points, 0)
print(root)