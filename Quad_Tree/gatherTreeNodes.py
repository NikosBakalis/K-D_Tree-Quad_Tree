general_list = []

def gather_tree_nodes(node):
    if node is None:
        return False
    if node.TopLeftChild is None and node.TopRightChild is None and node.BottomLeftChild is None and node.BottomRightChild is None:
        for point in node.points:
            general_list.append(point)
    else:
        return gather_tree_nodes(node.TopLeftChild), gather_tree_nodes(node.TopRightChild), gather_tree_nodes(node.BottomLeftChild), gather_tree_nodes(node.BottomRightChild)