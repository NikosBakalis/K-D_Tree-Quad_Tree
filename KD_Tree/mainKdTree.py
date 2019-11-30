import medianBuild
import searchPoint
import rebalance
import insert
import kNNQuery



points = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
dimensions = 2

root = medianBuild.kdTreeBuild(points, 0)  # Build the tree

insert.insertNode(root, (8, 2))
searchedPoint = searchPoint.kdTreeSearch(root, (8, 2))  # The point needs to be created first in order to be compared
# in if function
if searchedPoint['found']:
    print("Found")
else:
    print("Not Found")

print(kNNQuery.kNNSearch(root, (0,0), 7))
root = rebalance.balanceKdTree(root)

