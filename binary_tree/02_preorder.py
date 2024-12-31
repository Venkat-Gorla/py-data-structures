from node import Node

# Iterative preorder traversal
def preorder(root):
    if not root:
        return

    nodeStack = [root]

    while nodeStack:
        current = nodeStack.pop()
        print(current.data, end=' ')

        if current.right:
            nodeStack.append(current.right)

        if current.left:
            nodeStack.append(current.left)
# end preorder

# Driver code
def main():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(4)
    root.right.left = Node(3)
    root.right.right = Node(5)

    print("Preorder traversal of binary tree is")
    preorder(root)

main()

# output:
# Preorder traversal of binary tree is
# 2 1 4 3 5

