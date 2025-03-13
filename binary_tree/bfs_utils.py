# some reusable code for binary tree bfs (breadth first search) algorithm

# pending: add a function that returns one level of nodes each time it is called

from node import Node
from collections import deque

def bfs_generator(root):
    """
    BFS generator for binary tree
    Args:
        root: root of the binary tree
    Yields:
        The current node being visited in bfs
    """
    if root is None:
        return

    # the syntax looks a bit confusing, but we are still initializing
    # the queue with the root, not with a list containing the root
    node_queue = deque([root])

    while node_queue:
        current = node_queue.popleft()
        yield current
        if current.left:
            node_queue.append(current.left)
        if current.right:
            node_queue.append(current.right)

def _create_test_tree():
    # create a binary tree
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    return root

def _test_bfs_generator():
    root = _create_test_tree()

    print('BFS traversal of the binary tree is:')
    for current in bfs_generator(root):
        print(current.data, end=' ')
    print()

if __name__ == '__main__':
    _test_bfs_generator()

# Output:
# BFS traversal of the binary tree is:
# 1 2 3 4 5 6
