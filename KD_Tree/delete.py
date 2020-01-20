from KDTree import searchPoint
from KDTree import findMinimum
from KDTree.findMinimum import findMin


def deleteNode(root, point):
    searchedNode = searchPoint.kdTreeSearch(root, point)
    if searchedNode['found'] is False:
        print("Node to be deleted, Not Found")
    else:
        if searchedNode['node'].leftChild is None and searchedNode['node'].rightChild is None:
            if searchedNode['parentNode'].leftChild == searchedNode['node']:
                searchedNode['parentNode'].leftChild = None
            if searchedNode['parentNode'].rightChild == searchedNode['node']:
                searchedNode['parentNode'].rightChild = None
        elif searchedNode['node'].rightChild is not None:  # If node to be deleted has a right subtree
            minNode = findMin(searchedNode['node'].rightChild, searchedNode['depth'] % 2)

            # copy the minimum to the root
            searchedNode['node'].node = minNode.node
        # Recursively delete the minimum
            searchedNode['node'].rightChild = deleteNode(searchedNode['node'].rightChild, minNode.node)