# Given a Binary Tree, print left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from left side. Left view of following tree is 12, 10, 25.

#           12
#        /     \
#      10       30
#             /    \
#           25      40

from node import Node, print_node_path

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

# solution function
def get_left_view_nodes(root):
    output_list = []
    get_left_view(root, 0, output_list)
    return output_list

# test related code
def _create_test_tree():
    root = Node(12)
    root.left = Node(10)
    root.right = Node(30)
    root.right.left = Node(25)
    root.right.right = Node(40)
    return root

def _test_left_view():
    root = _create_test_tree()
    output_list = get_left_view_nodes(root)
    output_data_list = [node.data for node in output_list]
    assert output_data_list == [12, 10, 25]
    print("Get left view test passed")

    print("Left view of the binary tree is: ", end="")
    print_node_path(output_list)

if __name__ == "__main__":
    _test_left_view()

# output:
# Get left view test passed
# Left view of the binary tree is: 12 10 25
