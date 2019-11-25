# Test on PC No. 2
from recordtype import recordtype

# points = [(-3, 1), (1, 1), (-1, -5), (1, -1), (1, 2), (2, 2), (0.5, 2.7)]
points = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)]

qtNode = recordtype('qtNode', 'TopLeftChild TopRightChild BottomLeftChild BottomRightChild points x y')


def boundaries(points):
    points.sort(key=lambda tup: tup[0])
    mid_x = (points[0][0] + points[-1][0]) / 2
    points.sort(key=lambda tup: tup[1])
    mid_y = (points[0][1] + points[-1][1]) / 2
    return mid_x, mid_y


def build(points, max_nodes_per_quad):
    max_nodes_per_quad = 1  # TODO: This will be asked from the user
    mid_x, mid_y = boundaries(points)
    root = qtNode(None, None, None, None, points, mid_x, mid_y)
    # print(root)
    insert(root, max_nodes_per_quad)
    return root


def insert(node, max_nodes_per_quad):
    cross_x = node.x
    cross_y = node.y
    lista = node.points
    Top_Left_List = []
    Top_Right_List = []
    Bottom_Left_List = []
    Bottom_Right_List = []
    for point in lista:
        # print(point)
        if point[0] <= cross_x and point[1] >= cross_y:
            Top_Left_List.append(point)
        if cross_x < point[0] and point[1] > cross_y:
            Top_Right_List.append(point)
        if point[0] < cross_x and point[1] < cross_y:
            Bottom_Left_List.append(point)
        if cross_x <= point[0] and point[1] <= cross_y:
            Bottom_Right_List.append(point)
    lista.clear()

    if len(Top_Left_List) > 0:
        Top_Left_List.sort(key=lambda tup: tup[0])
        kapou_x_TL = Top_Left_List[0][0]
        Top_Left_List.sort(key=lambda tup: tup[1])
        kapou_y_TL = Top_Left_List[-1][1]

        Top_Left_Child = qtNode(None, None, None, None, Top_Left_List, (cross_x + kapou_x_TL) / 2, (cross_y + kapou_y_TL) / 2)
        node.TopLeftChild = Top_Left_Child
        if len(Top_Left_List) > max_nodes_per_quad:
            insert(Top_Left_Child, max_nodes_per_quad)

    if len(Top_Right_List) > 0:
        Top_Right_List.sort(key=lambda tup: tup[0])
        kapou_x_TR = Top_Right_List[-1][0]
        Top_Right_List.sort(key=lambda tup: tup[1])
        kapou_y_TR = Top_Right_List[-1][1]

        Top_Right_Child = qtNode(None, None, None, None, Top_Right_List, (cross_x + kapou_x_TR) / 2, (cross_y + kapou_y_TR) / 2)
        node.TopRightChild = Top_Right_Child
        if len(Top_Right_List) > max_nodes_per_quad:
            insert(Top_Right_Child, max_nodes_per_quad)

    if len(Bottom_Left_List) > 0:
        Bottom_Left_List.sort(key=lambda tup: tup[0])
        kapou_x_BL = Bottom_Left_List[0][0]
        Bottom_Left_List.sort(key=lambda tup: tup[1])
        kapou_y_BL = Bottom_Left_List[0][1]

        Bottom_Left_Child = qtNode(None, None, None, None, Bottom_Left_List, (cross_x + kapou_x_BL) / 2, (cross_y + kapou_y_BL) / 2)
        node.BottomLeftChild = Bottom_Left_Child
        if len(Bottom_Left_List) > max_nodes_per_quad:
            insert(Bottom_Left_Child, max_nodes_per_quad)

    if len(Bottom_Right_List) > 0:
        Bottom_Right_List.sort(key=lambda tup: tup[0])
        kapou_x_BR = Bottom_Right_List[-1][0]
        Bottom_Right_List.sort(key=lambda tup: tup[1])
        kapou_y_BR = Bottom_Right_List[0][1]

        Bottom_Right_Child = qtNode(None, None, None, None, Bottom_Right_List, (cross_x + kapou_x_BR) / 2, (cross_y + kapou_y_BR ) / 2)
        node.BottomRightChild = Bottom_Right_Child
        if len(Bottom_Right_List) > max_nodes_per_quad:
            insert(Bottom_Right_Child, max_nodes_per_quad)


def traverse_tree(node, point, max_nodes_per_quad):
    if node.TopLeftChild == None and node.TopRightChild == None and node.BottomLeftChild == None and node.BottomRightChild == None:
        node.points.append(point)
        if len(node.points) > max_nodes_per_quad:
            print(node.points)
            insert(node, max_nodes_per_quad)
    cross_x = node.x
    cross_y = node.y
    if point[0] <= cross_x and point[1] >= cross_y:
        traverse_tree(node.TopLeftChild, point, max_nodes_per_quad)
    if cross_x < point[0] and point[1] > cross_y:
        traverse_tree(node.TopRightChild, point, max_nodes_per_quad)
    if point[0] < cross_x and point[1] < cross_y:
        traverse_tree(node.BottomLeftChild, point, max_nodes_per_quad)
    if cross_x <= point[0] and point[1] <= cross_y:
        traverse_tree(node.BottomRightChild, point, max_nodes_per_quad)


def rebalance(node):
    if node.TopLeftChild == None and node.TopRightChild == None and node.BottomLeftChild == None and node.BottomRightChild == None:
        for point in node.points:
            general_list.append(point)
    else:
        rebalance(node.TopLeftChild)
        rebalance(node.TopRightChild)
        rebalance(node.BottomLeftChild)
        rebalance(node.BottomRightChild)

    return build(general_list, 1)


root = build(points, 1)
print(root)
# traverse_tree(root, (2, 2), 1)
# print(root)
general_list = []
# root = rebalance(root)
