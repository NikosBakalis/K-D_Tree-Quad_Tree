import searchPoint


def delete(root, point):
    node = searchPoint.kdTreeSearch(root, point)
    if node['found'] is False:
        print("Node to be deleted, Not Found")
    else:
        if node['node'].leftChild is None and node['node'].rightChild is None:
            if node['parentNode'].leftChild == node['node']:
                node['parentNode'].leftChild
            if node['parentNode'].rightChild == node['node']:
                node['parentNode'].rightChild = None
        else:
            print("Not None")
