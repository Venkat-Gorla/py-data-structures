# some reusable code for inorder traversal

from node import Node

# inorder traversal using generator and yield
def inorder_generator(root):
    current = root
    nodeStack = []

    while current or nodeStack:
        while current:
            nodeStack.append(current)
            current = current.left

        current = nodeStack.pop()
        yield current
        current = current.right

# inorder generator using Morris traversal (threaded binary tree)
# it uses constant extra space but makes temp changes to the tree, so the 
# tree cannot be read-only
def inorder_threaded_generator(root):
    current = root

    while current:
        if current.left is None:
            yield current
            current = current.right
        else:
            predecessor = _get_inorder_predecessor(current)

            if predecessor.right is None:
                # we are going down the tree, so make a thread to current
                predecessor.right = current
                current = current.left
            else:
                # thread connection is already created, we are going up the tree after
                # visiting the left subtree, so yield current and remove the thread
                predecessor.right = None
                yield current
                current = current.right
# end inorder_threaded_generator

# internal function for Morris inorder traversal
def _get_inorder_predecessor(current):
    predecessor = current.left
    while predecessor.right and predecessor.right != current:
        predecessor = predecessor.right
    return predecessor

# internal functions for testing
def _test_inorder_threaded_generator(root):
    print("Inorder traversal using Morris traversal generator:")
    for current in inorder_threaded_generator(root):
        print(current.data, end=" ")
    print()

def _test_inorder_generator(root):
    print("Inorder traversal using normal generator:")
    for current in inorder_generator(root):
        print(current.data, end=" ")
    print()

def _create_test_tree():
    # create a test tree for inorder traversal
    #       4
    #      / \
    #     2   5
    #    / \   \
    #   1   3   6
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.right = Node(6)
    return root

if __name__ == "__main__":
    root = _create_test_tree()
    _test_inorder_threaded_generator(root)
    print()
    _test_inorder_generator(root)

# output:
# Inorder traversal using Morris traversal generator:
# 1 2 3 4 5 6

# Inorder traversal using normal generator:
# 1 2 3 4 5 6
