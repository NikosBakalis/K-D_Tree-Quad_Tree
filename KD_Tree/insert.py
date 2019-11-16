import searchPoint


def insertNode(root, point):
    searchedNode = searchPoint.kdTreeSearch(root, point)
    if searchedNode['found']:
        print("Node already exists")
        return None
    else:
        depth = searchedNode['depth']
        axis = depth % 2  # 2 cause this tree has 2 dimensions
        node = searchedNode['parentNode']
        if axis == 0:
            node.leftChild = point
        else:
            node.rightChild = point
