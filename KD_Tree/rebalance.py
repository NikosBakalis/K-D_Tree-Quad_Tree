import medianBuild

rebuildPoints = []
dimensions = 2


def gatherTreeNodes(node):
    if node is None:
        return None
    rebuildPoints.append(node.node)	# Append every point
    return gatherTreeNodes(node.leftChild), gatherTreeNodes(node.rightChild)


def balanceKdTree(node):
    gatherTreeNodes(node)  # Gather all the nodes of the tree
    root = medianBuild.kdTreeBuild(rebuildPoints, 0)  # Rebuild the tree
    return root # Return new root
