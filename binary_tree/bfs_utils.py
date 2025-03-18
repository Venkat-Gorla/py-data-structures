# some reusable code for binary tree bfs (breadth first search) algorithm

from node import Node, print_node_path
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

# reverse bfs generator function
def reverse_bfs_generator(root):
    if root is None:
        return

    node_queue = deque([root])
    reverse_bfs = deque()

    while node_queue:
        current = node_queue.popleft()
        reverse_bfs.appendleft(current)

        if current.right:
            node_queue.append(current.right)
        if current.left:
            node_queue.append(current.left)

    for node in reverse_bfs:
        yield node

def bfs_levels_generator(root):
    """
    BFS levels generator for binary tree
    Args:
        root: root of the binary tree
    Yields:
        Each level of nodes in the tree, one at a time as a tuple
    """
    if root is None:
        return

    node_queue = deque([root])
    while node_queue:
        level_size = len(node_queue)
        yield tuple(node_queue[i] for i in range(level_size))

        for _ in range(level_size):
            current = node_queue.popleft()
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
    print_node_path(bfs_generator(root))

def _test_reverse_bfs_generator():
    root = _create_test_tree()
    print('\nReverse BFS traversal of the binary tree is:')
    print_node_path(reverse_bfs_generator(root))

def _test_bfs_levels_generator():
    root = _create_test_tree()

    print('\nPrinting levels of the binary tree:')
    for level in bfs_levels_generator(root):
        assert isinstance(level, tuple)
        print('Level:', end=' ')
        for node in level:
            print(node.data, end=' ')
        print()

if __name__ == '__main__':
    _test_bfs_generator()
    _test_reverse_bfs_generator()
    _test_bfs_levels_generator()

# Output:
# BFS traversal of the binary tree is:
# 1 2 3 4 5 6

# Reverse BFS traversal of the binary tree is:
# 4 5 6 2 3 1

# Printing levels of the binary tree:
# Level: 1
# Level: 2 3
# Level: 4 5 6
