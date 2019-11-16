dimensions = 2


def kdTreeSearch(node, point, depth=0, previous_node=None):
    if node is None:
        return {  # A dictionary is returned cause it would be more helpful to know the parent node for insert function.
            'found': False,
            'parentNode': previous_node
        }
    if node.node == point:
        return {
            'found': True
        }
    axis = depth % dimensions
    if (point[axis] < node.node[axis]):
        previous_node = node
        return kdTreeSearch(node.leftChild, point, depth + 1, previous_node)  # Search left sub tree
    else:
        previous_node = node
        return kdTreeSearch(node.rightChild, point, depth + 1, previous_node)  # Search right sub tree
