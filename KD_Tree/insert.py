import medianBuild
import searchPoint
import rebalance


# insert

def insertNode(root, point):
    searchedNode = searchPoint.kdTreeSearch(root, point)
    if searchedNode['found']:
        print("Node already exists")
        return None

    print(searchedNode['parent'])
