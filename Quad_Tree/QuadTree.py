import boundaries
import build
import insert
import traverseTree
import gatherTreeNodes
import rebalance
import csv

x_y_values = []
with open('points', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        x_y_values.append((int(row[0]), int(row[1])))
print(x_y_values)

points = x_y_values

# points = [(-3, 1), (1, 1), (-1, -5), (1, -1), (1, 2), (2, 2), (0.5, 2.7)]
points = x_y_values # [(1, 1), (1, -1), (-1, 1), (-1, -1), (2, 3), (4, 1), (-1, -5), (-3, 9)]    # For some reason last node pops an error, exclude it to run!
dimensions = 2
print("test")

boundaries.boundaries(points)
print("test")
root = build.build(points, 1)
traverseTree.traverse_tree(root, (2, 2), 1)
print(root)
general_list = []
root = rebalance.rebalance(root, 1)
print(root)
