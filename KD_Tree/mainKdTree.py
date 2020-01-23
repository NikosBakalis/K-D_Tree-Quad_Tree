import medianBuild
import searchPoint
import rebalance
import insert
import kNNQuery
import delete

points = []
file = open("test.txt","r")
for line in file:
    points.append(eval(line))
file.close()

print(points)
dimensions = 2

root = medianBuild.kdTreeBuild(points, 0)  # Build the tree

print(points)
point = points.pop(500)
print(searchPoint.kdTreeSearch(root, point,0))
delete.deleteNode(root,point,0)
print(searchPoint.kdTreeSearch(root, point,0))


# insert.insertNode(root, (8, 2))
# searchedPoint = searchPoint.kdTreeSearch(root, (7, 2))  # The point needs to be created first in order to be compared
# # in if function
# if searchedPoint['found']:
#     print("Found")
# else:
#     print("Not Found")
#
# delete.deleteNode(root,(7,2))
#
# searchedPoint = searchPoint.kdTreeSearch(root, (7,2))
# if searchedPoint['found']:
#     print("Found")
# else:
#     print("Not Found")

