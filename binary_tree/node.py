class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def is_leaf(self):
        return not (self.left or self.right)

def print_node_path(path):
    """
    Given a node list, print their data contents
    """
    for node in path:
        print(node.data, end=" ")
    print()

