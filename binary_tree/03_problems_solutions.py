
# Here we will explore a collection of common binary tree problems and their solutions

#----------------------------------------
# Given a binary tree, print all root to leaf paths

from node import Node, print_node_path
from traversal_utils import postorder_paths_generator

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

def create_tree_for_root_leaf_paths():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    return root

def main_root_to_leaf_paths():
    root = create_tree_for_root_leaf_paths()

    test_root_to_leaf_paths(root)

if __name__ == '__main__':
    main_root_to_leaf_paths()

# output:
# Printing root to leaf paths of binary tree:
# 1 2
# 1 3 4
# 1 3 5

#----------------------------------------
# Given a binary tree, print all root to leaf paths
# if you ever care about solving this problem using iteration, there is a neat solution
# using postorder generator
def test_postorder_root_to_leaf_paths(root):
    print("\nPrinting root to leaf paths of binary tree using postorder generator:")
    for node_path, current_node in postorder_paths_generator(root):
        if current_node.is_leaf():
            print_node_path(node_path)

def main_postorder_root_to_leaf_paths():
    root = create_tree_for_root_leaf_paths()
    test_postorder_root_to_leaf_paths(root)

if __name__ == '__main__':
    main_postorder_root_to_leaf_paths()

# output:
# Printing root to leaf paths of binary tree using postorder generator:
# 1 2
# 1 3 4
# 1 3 5

#----------------------------------------
# given a binary tree and a key (that may or may not be present in it) find the key's Inorder successor

from node import Node

# unlike C++, python doesn't have reference variables, so we use a list of one element
# to track the previous node when doing Inorder traversal
def find_inorder_successor(root, key, previous = [None]):
    if not root:
        return None

    left = find_inorder_successor(root.left, key, previous)
    if left:
        return left

    if previous[0] and previous[0].data == key:
        return root

    previous[0] = root

    return find_inorder_successor(root.right, key, previous)

def test_find_inorder_successor(root, key):
    successor = find_inorder_successor(root, key)
    if successor:
        print(f"Inorder successor of {key} is {successor.data}")
    else:
        print(f"Inorder successor of {key} is Not found")

def main_inorder_successor():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    print()
    input = [2, 1, 3]
    for key in input:
        test_find_inorder_successor(root, key)

if __name__ == '__main__':
    main_inorder_successor()

# output:
# Inorder successor of 2 is 1
# Inorder successor of 1 is 3
# Inorder successor of 3 is Not found

#----------------------------------------
# Print all k-sum paths in a binary tree
# A binary tree and a number k are given. Print every path in the tree with sum of the nodes in the path as k.
# A path can start from any node and end at any node, i.e. they need not be root node and leaf node; and negative numbers can also be there in the tree.

def find_subarrays_with_k_sum(input_path, K, output_paths):
    running_sum = 0

    for index in range(len(input_path) - 1, -1, -1):
        running_sum += input_path[index]
        if running_sum == K:
            output_paths.append(input_path[index:])

# solution helper function
# we will use a slight variation of the root to leaf paths recursive function, we keep
# track of the current path in the tree, when a new node gets appended to the path, we
# check the sum condition starting with the last node of the path
def k_sum_path_helper(root, K, current_path, output_paths):
    if not root:
        return

    current_path.append(root.data)

    k_sum_path_helper(root.left, K, current_path, output_paths)
    k_sum_path_helper(root.right, K, current_path, output_paths)
    find_subarrays_with_k_sum(current_path, K, output_paths)

    current_path.pop()

# solution function
def print_k_sum_paths(root, K):
    current_path = []
    output_paths = []
    k_sum_path_helper(root, K, current_path, output_paths)
    print(f"\nPrinting all k={K} sum paths in the binary tree:")
    print(output_paths, end=" ")
    print()

def create_tree_for_k_sum_paths():
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right = Node(-1)
    root.right.left = Node(4)
    root.right.left.left = Node(1)
    root.right.left.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(2)

    return root

def test_k_sum_paths():
    root = create_tree_for_k_sum_paths()
    print_k_sum_paths(root, 5)

if __name__ == '__main__':
    test_k_sum_paths()

# output:
# Printing all k=5 sum paths in the binary tree:
# [[3, 2], [3, 1, 1], [1, 3, 1], [4, 1], [1, -1, 4, 1], [-1, 4, 2], [5], [1, -1, 5]]

