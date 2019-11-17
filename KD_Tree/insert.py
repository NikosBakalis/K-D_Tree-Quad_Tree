    import searchPoint


    def insertNode(root, point):
        searchedNode = searchPoint.kdTreeSearch(root, point)
        if searchedNode['found']:
            print("Node already exists")
            return None
        else:
            depth = searchedNode['depth']
            axis = depth % 2  # 2 cause this tree has 2 dimensions
            node = searchedNode['parentNode']
            if point[axis] < node.node[axis]:
                node = (node.node, node.leftChild, point)
            else:
                node = (node.node, point, node.rightChild)

