# Given a Binary Tree, print left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from left side. Left view of following tree is 12, 10, 25.

#           12
#        /     \
#      10       30
#             /    \
#           25      40

# topics covered:
# recursive solution
# iterative solution using bfs levels generator

from node import Node, print_node_path
from bfs_utils import bfs_levels_generator

# recursive solution function
def get_left_view_nodes(root):
    output_list = []
    get_left_view(root, 0, output_list)
    return output_list

# solution helper function
# keep track of max level seen so far and add the first node at every level that is > max
def get_left_view(root, current_level, output_list, max_level = [-1]):
    if not root:
        return

    if current_level > max_level[0]:
        max_level[0] = current_level
        output_list.append(root)

    get_left_view(root.left, current_level + 1, output_list, max_level)
    get_left_view(root.right, current_level + 1, output_list, max_level)

# alternate iterative solution using bfs levels generator
def get_left_view_nodes_bfs(root):
    output_list = []
    for level in bfs_levels_generator(root):
        output_list.append(level[0])
    return output_list

# test related code
def _create_test_tree():
    root = Node(12)
    root.left = Node(10)
    root.right = Node(30)
    root.right.left = Node(25)
    root.right.right = Node(40)
    return root

def _validate_output(expected_output, output_list_rec, output_list_bfs):
    output_data_list_rec = [node.data for node in output_list_rec]
    assert output_data_list_rec == expected_output

    output_data_list_bfs = [node.data for node in output_list_bfs]
    assert output_data_list_bfs == expected_output

    print("Get left view using recursion and iteration tests passed")

def _test_left_view():
    root = _create_test_tree()
    output_list_rec = get_left_view_nodes(root)
    output_list_bfs = get_left_view_nodes_bfs(root)
    _validate_output([12, 10, 25], output_list_rec, output_list_bfs)

    print("Left view of the binary tree is: ", end="")
    print_node_path(output_list_rec)

if __name__ == "__main__":
    _test_left_view()

# output:
# Get left view using recursion and iteration tests passed
# Left view of the binary tree is: 12 10 25
