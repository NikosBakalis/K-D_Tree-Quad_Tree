import math
import functions
dimensions = 2
kNNPoints = []
minimumDistance = float('inf')

def euclideanDistance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


def kNNSearch(node, queryPoint, k):
    reverseSearch(node, queryPoint, k) # We have to choose what this function will return
    if len(kNNPoints) < k:
        print("sorry,not enough points")
    else:
        print("enough points")
    return kNNPoints

def reverseSearch(node, queryPoint, k):
    global minimumDistance
    if node is None:
        return

    if functions.isLeaf(node) is True:
        for i in range(len(node.points)):
            distance = euclideanDistance(node.points[i], queryPoint)
            if len(kNNPoints) < k or distance < minimumDistance:
                if len(kNNPoints) == k:
                    kNNPoints.pop(-1)
                kNNPoints.append((node.points[i], distance))     # Append (node, distance) in this list
                minimumDistance = kNNPoints[-1][1]  # last element distance(furthest distance)
    else:
        if queryPoint[0] <= node.x and queryPoint[1] >= node.y:
            return reverseSearch(node.TopLeftChild, queryPoint, k), reverseSearch(node.BottomRightChild, queryPoint, k), reverseSearch(node.TopRightChild, queryPoint, k), reverseSearch(node.BottomLeftChild, queryPoint, k)
        elif queryPoint[0] >= node.x and queryPoint[1] <= node.y:
            return reverseSearch(node.BottomRightChild, queryPoint, k), reverseSearch(node.TopLeftChild, queryPoint, k), reverseSearch(node.TopRightChild, queryPoint, k), reverseSearch(node.BottomLeftChild, queryPoint, k)
        elif queryPoint[0] > node.x and queryPoint[1] > node.y:
            return reverseSearch(node.TopRightChild, queryPoint, k), reverseSearch(node.TopLeftChild, queryPoint, k), reverseSearch(node.BottomRightChild, queryPoint, k), reverseSearch(node.BottomLeftChild, queryPoint, k)
        elif queryPoint[0] < node.x and queryPoint[1] < node.y:
            return reverseSearch(node.BottomLeftChild, queryPoint, k), reverseSearch(node.TopLeftChild, queryPoint, k), reverseSearch(node.BottomRightChild, queryPoint, k), reverseSearch(node.TopRightChild, queryPoint, k)