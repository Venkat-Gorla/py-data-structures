# given a binary tree, print it's bottom view
# sample tree:

#           20
#         /     \
#       8        22
#     /   \     /   \
#   5      3   4     25
#         / \
#       10   14 

# expected output:
# 5 10 3 4 14 25

# when getting top or bottom view of a binary tree, think of the vertical distance of every node in the tree.
# root has distance 0, left child of a node is (parent - 1) and right child is (parent + 1).
# if two or more nodes have the same vertical distance, the one at the bottom most level will be visible and all other nodes will be hidden. So that is how you arrive at the bottom view.

# same logic applies to the top view, if multiple nodes have the same vertical distance, the node at the topmost level will be visible and all other nodes below it will be hidden.

from node import Node

# recursive solution
# create a hash table of vertical distances and their respective max horizontal levels. Key is vertical distance and value is the max horizontal level for that distance.
# once the hash table is created, do a simple traversal of the tree and get all the nodes whose level is the max level for that vertical distance.
def get_bottom_view(root):
    distance_max_level = {}
    _update_distance_table(root, 0, 0, distance_max_level)

    bottom_view = []

    def _get_bottom_view(root, vertical_dist, current_level):
        if root is None:
            return

        _get_bottom_view(root.left, vertical_dist - 1, current_level + 1)
        _get_bottom_view(root.right, vertical_dist + 1, current_level + 1)

        if current_level == distance_max_level[vertical_dist]:
            bottom_view.append(root)

    _get_bottom_view(root, 0, 0)
    return bottom_view

# helper function to create vertical distance max level table
def _update_distance_table(
    root: Node | None,
    vertical_dist: int, 
    current_level: int, 
    distance_max_level: dict[int, int]
) -> None:
    """
    Updates a hash table mapping each vertical distance to the maximum level reached in a binary tree.
    """

    if root is None:
        return

    distance_max_level[vertical_dist] = max(
        current_level, 
        distance_max_level.get(vertical_dist, -1)
    )

    _update_distance_table(root.left, vertical_dist - 1, current_level + 1, distance_max_level)
    _update_distance_table(root.right, vertical_dist + 1, current_level + 1, distance_max_level)
# end function

# test related code
def _test_get_bottom_view():
    root = _create_test_tree()
    bottom_view = get_bottom_view(root)
    print("Bottom view of the tree is:")
    for node in bottom_view:
        print(node.data, end=" ")
    print()

    assert [node.data for node in bottom_view] == [5, 10, 14, 3, 4, 25]
    print("Get bottom view test passed!")

def _create_test_tree():
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    return root

if __name__ == "__main__":
    _test_get_bottom_view()

# output:
# Bottom view of the tree is:
# 5 10 14 3 4 25
# Get bottom view test passed!
