import build
import gatherTreeNodes


def rebalance(node):
    gatherTreeNodes.gather_tree_nodes(node)
    root = build.build(gatherTreeNodes.general_list, 1)
    return root
