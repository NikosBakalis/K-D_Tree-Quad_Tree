dimensions = 2


def kdTreeSearch(node, point, depth=0):
    if node is None:
        return False
    if node.node == point:
        return True

    axis = depth % dimensions
    if (point[axis] < node[0][axis]):
        return kdTreeSearch(node.leftChild, point, depth + 1)  # Search left sub tree
    else:
        return kdTreeSearch(node.rightChild, point, depth + 1)  # Search right sub tree
