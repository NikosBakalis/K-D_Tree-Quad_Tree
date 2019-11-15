import medianBuild
import searchPoint
import rebalance

points = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
dimensions = 2

root = medianBuild.kdTreeBuild(points, 0)  # Build the tree

if (searchPoint.kdTreeSearch(root, (8, 1))):
    print("Found")
else:
    print("Not Found")

root = rebalance.balanceKdTree(root)

