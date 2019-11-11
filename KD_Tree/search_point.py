import median_build

points = [(7,2), (5,4), (9,6), (4,7), (8,1), (2,3)]
dimensions = 2

root = median_build.kdTreeBuild(points, 0)

def kdTreeSearch(node, point, depth = 0):
    if node is None:
        return False
    if node.node == point:
        return True

    axis = depth % dimensions
    if (point[axis] < node[0][axis]):
        return kdTreeSearch(node.leftChild, point, depth + 1)
    else:
        return kdTreeSearch(node.rightChild, point, depth + 1)


if (kdTreeSearch(root, (3, 1))):
    print("Found")
else:
    print("Not Found")