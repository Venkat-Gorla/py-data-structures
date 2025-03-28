# Extract Leaves of a Binary Tree into a Doubly Linked List and also return the remaining tree structure

# so your function must return both the root of the modified tree and the head of the DLL containing the leaves

# Given a Binary Tree, extract all leaves of it into a Doubly Linked List (DLL). Note that the DLL need to be created in-place.
# Assume that the node structure of DLL and Binary Tree is same, only the meaning of left and right pointers are different.
# In DLL, left means previous pointer and right means next pointer.

# Test case 1:
# Let the following be input binary tree
#         1
#      /     \
#     2       3
#    / \       \
#   4   5       6
#  / \         / \
# 7   8       9   10


# Output:
# Doubly Linked List
# 7<->8<->5<->9<->10

# Modified Tree:
#         1
#      /     \
#     2       3
#    /         \
#   4           6

from node import Node, print_tree

# recursive solution
# traverse the tree, for every leaf node encountered, push it into your output DLL
# inside the parent node of the leaf, set it's respective child pointer to None
def extract_helper(root, dll_list):
    if root is None:
        return False
    elif root.is_leaf():
        return extract_leaf_node(root, dll_list)
    else:
        # since the leaf DLL will be created in reverse order, to maintain left to right ordering,
        # we visit the right sub-tree first and then the left sub-tree
        if extract_helper(root.right, dll_list):
            root.right = None
        if extract_helper(root.left, dll_list):
            root.left = None
        return False

def extract_leaf_node(root, dll_list):
    if dll_list[0] is None:
        dll_list[0] = root
    else:
        # this is similar to stack push, so the list will be created in reverse order
        root.right = dll_list[0]
        dll_list[0].left = root
        dll_list[0] = root
    return True

# wrapper function for clients
def extract_leaves(root):
    if root is None:
        return root, None

    dll_list = [None]
    if extract_helper(root, dll_list):
        root = None

    return root, dll_list[0]

# test code
def _test_extract_leaves():
    root = _create_test_tree()
    print("Original Tree:")
    print_tree(root)
    root, dll_head = extract_leaves(root)
    print("\nModified Tree:")
    print_tree(root)
    print("\nDLL:")
    _print_validate_dll(dll_head)

def _create_test_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)
    return root

def _print_validate_dll(head):
    current = head
    fwd_list = []
    tail = None
    while current is not None:
        print(current.data, end=" ")
        fwd_list.append(current.data)
        tail = current
        current = current.right

    reverse_list = []
    current = tail
    while current is not None:
        reverse_list.append(current.data)
        current = current.left

    assert fwd_list == reverse_list[::-1]
    print("\nDLL fwd and reverse validation passed")

if __name__ == '__main__':
    _test_extract_leaves()

# output:
# Original Tree:
# -->1 (root)
#    |-->2 (L)
#    |   |-->4 (L)
#    |   |   |-->7 (L)
#    |   |   |-->8 (R)
#    |   |-->5 (R)
#    |-->3 (R)
#    |   |-->6 (R)
#    |   |   |-->9 (L)
#    |   |   |-->10 (R)

# Modified Tree:
# -->1 (root)
#    |-->2 (L)
#    |   |-->4 (L)
#    |-->3 (R)
#    |   |-->6 (R)

# DLL:
# 7 8 5 9 10
# DLL fwd and reverse validation passed
