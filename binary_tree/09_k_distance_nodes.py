# Print all nodes that are at distance k from a leaf node

# Given a Binary Tree and a positive integer k, print all nodes that are at distance k from a (any/ some) leaf node.

# Here k distance from a leaf means k levels higher than a leaf node. For example if k is more than the height of the Binary Tree, then nothing should be printed. Expected time complexity is O(n) where n is the number nodes in the given Binary Tree.

#             1
#           /  \
#          2      3
#        /  \    / \
#       4    5  6   7
#                \
#                 8

# Leaf nodes: 4 5 8 7
# Nodes at distance 1 --> 2 6 3
# Nodes at distance 2 --> 3 1
# Nodes at distance 3 --> 1
# Nodes at distance 4 --> None

from node import Node

# recursive solution
# use a hash set to store the various levels in which a leaf is present
def get_k_distance_nodes(root, K: int, output_list):
    current_level = 0
    leaf_level_set = set()
    get_k_distance_helper(root, K, current_level, leaf_level_set, output_list)

def get_k_distance_helper(
    root, 
    K: int, 
    current_level, 
    leaf_level_set: set, 
    output_list
):
    if root is None:
        return
    elif root.is_leaf():
        if current_level not in leaf_level_set:
            leaf_level_set.add(current_level)
        return

    get_k_distance_helper(root.left, K, current_level + 1, leaf_level_set, output_list)
    get_k_distance_helper(root.right, K, current_level + 1, leaf_level_set, output_list)

    if current_level + K in leaf_level_set:
        output_list.append(root)

# test code
def _test_k_distance_nodes():
    root = _create_test_tree()
    for K in range(1, 5):
        output_list = []
        get_k_distance_nodes(root, K, output_list)
        print(f"Nodes at distance {K} from a leaf node: {[node.data for node in output_list]}")

def _create_test_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    return root

if __name__ == "__main__":
    _test_k_distance_nodes()

# Output:
# Nodes at distance 1 from a leaf node: [2, 6, 3]
# Nodes at distance 2 from a leaf node: [3, 1]
# Nodes at distance 3 from a leaf node: [1]
# Nodes at distance 4 from a leaf node: []
