
# Here we will explore a collection of common binary tree problems and their solutions

#----------------------------------------
# Given a binary tree, print all root to leaf paths

from node import Node, print_node_path

# solution helper function
def root_to_leaf_paths(root, output_path):
    if not root:
        return

    output_path.append(root)

    if root.is_leaf():
        print_node_path(output_path)
    else:
        root_to_leaf_paths(root.left, output_path)
        root_to_leaf_paths(root.right, output_path)

    output_path.pop()

def print_root_to_leaf_paths(root):
    output_path = []
    root_to_leaf_paths(root, output_path)

def test_root_to_leaf_paths(root):
    print("Printing root to leaf paths of binary tree:")
    print_root_to_leaf_paths(root)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)

    test_root_to_leaf_paths(root)

main()

# output:
# Printing root to leaf paths of binary tree:
# 1 2
# 1 3 4
# 1 3 5

#----------------------------------------

