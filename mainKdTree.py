import medianBuild
import searchPoint
import rebalance
import insert

import csv

x_y_values = []
with open('points', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        x_y_values.append((int(row[0]), int(row[1])))
print(x_y_values)

points = x_y_values

dimensions = 2

root = medianBuild.kdTreeBuild(points, 0)  # Build the tree

insert.insertNode(root, (8, 2))
searchedPoint = searchPoint.kdTreeSearch(root, (8, 2))  # The point needs to be created first in order to be compared
# in if function
if searchedPoint['found']:
    print("Found")
else:
    print("Not Found")



root = rebalance.balanceKdTree(root)

