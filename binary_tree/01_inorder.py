# Inorder traversal using iteration and generator "yield"

from node import Node

# Iterative Inorder traversal
def inorder_iter(root):
    current = root
    nodeStack = []

    while current or nodeStack:
        while current:
            nodeStack.append(current)
            current = current.left

        current = nodeStack.pop()
        print(current.data, end=' ')
        current = current.right
#end Inorder

# using generator and yield
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

def test_generator(root):
    for current in inorder_generator(root):
        print(current.data, end=' ')

# Driver code
# Note: python doesn't have the concept of a 'main' function, this is
# just to satisfy the C++ enthusiasts :)
def main():
    # create BST to illustrate the sorted nature of Inorder
    root = Node(2)
    root.left = Node(1)
    root.right = Node(4)
    root.right.left = Node(3)
    root.right.right = Node(5)

    print("Inorder traversal of binary tree is")
    inorder_iter(root)

    print("\n\nInorder traversal using generator is")
    test_generator(root)

main()

# output:
# Inorder traversal of binary tree is
# 1 2 3 4 5

# Inorder traversal using generator is
# 1 2 3 4 5

