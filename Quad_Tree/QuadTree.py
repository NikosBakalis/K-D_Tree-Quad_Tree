# Test on PC No. 2
import boundaries
import build
import insert
import traverseTree
import gatherTreeNodes
import rebalance


# points = [(-3, 1), (1, 1), (-1, -5), (1, -1), (1, 2), (2, 2), (0.5, 2.7)]
points = [(1, 1), (1, -1), (-1, 1), (-1, -1), (2, 3), (4, 1), (-1, -5), (-3, 9), (6, -1)]   # For some reason last node pops an error, exclude it to run!
dimensions = 2
print("test")

boundaries.boundaries(points)
print("test")
root = build.build(points, 1)
traverseTree.traverse_tree(root, (2, 2), 1)
print(root)
general_list = []
root = rebalance.rebalance(root)
print(root)
