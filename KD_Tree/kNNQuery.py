import math
dimensions = 2
kNNPoints = []


def euclideanDistance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


def kNNSearch(node, queryPoint, k, depth = 0, minimumDistance = float('inf')):
    if node is None:
        return kNNPoints

    distance = euclideanDistance(node.node, queryPoint)
    if (distance < minimumDistance) | (len(kNNPoints) < k):
        minimumDistance = distance
        if len(kNNPoints) == k:
            kNNPoints.pop(0)
        kNNPoints.append(node.node)
    axis = depth % dimensions
    if queryPoint[axis] < node.node[axis]:
        return kNNSearch(node.leftChild, queryPoint, k, depth + 1, minimumDistance)  # Search left sub tree
    else:
        return kNNSearch(node.rightChild, queryPoint, k, depth + 1, minimumDistance)  # Search right sub tree
