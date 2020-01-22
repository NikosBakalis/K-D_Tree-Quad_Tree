import searchPoint
from medianBuild import kdNode


def insertNode(root, point):
    searchedNode = searchPoint.kdTreeSearch(root, point)
    if searchedNode['found']:
        print("Node already exists")
        return None
    else:
        depth = searchedNode['depth']
        axis = depth % 2  # tree has 2 dimensions
        node = searchedNode['parentNode']
        if point[axis] < node.node[axis]:
            node.leftChild = kdNode(point, None, None)
        else:
            node.rightChild = kdNode(point, None, None)