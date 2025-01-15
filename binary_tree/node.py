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

def print_tree(node, level=0, label="(root)"):
    """
    Print the tree structure for visualization, follows preorder
    """
    if node is None:
        return

    for _ in range(level):
        print("   |", end="")

    print(f"-->{node.data} {label}")

    print_tree(node.left, level + 1, "(L)")
    print_tree(node.right, level + 1, "(R)")

