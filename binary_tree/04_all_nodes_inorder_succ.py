# Populate Inorder Successor for all nodes

# Given a Binary Tree where each node has following structure, write a function to populate next pointer for all nodes. The next pointer for every node should be set to point to inorder successor.

# struct Node
# {
#   int data;
#   Node* left;
#   Node* right;
#   Node* next;
# }

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

# solution: reverse inorder traversal and keep track of previous pointer using single element list
def populate_inorder_successor(root, previous=[None]):
    if root is None:
        return

    populate_inorder_successor(root.right, previous)
    root.next = previous[0]
    previous[0] = root
    populate_inorder_successor(root.left, previous)

def print_inorder_successor(root):
    if root is None:
        return

    current = root
    while current.left:
        current = current.left

    print("Printing inorder successors using next pointer")
    while current:
        print(f"{current.data} -> {current.next.data if current.next else None}")
        current = current.next

def test_inorder_successor():
    root = Node(10)
    root.left = Node(8)
    root.right = Node(12)
    root.left.left = Node(3)

    populate_inorder_successor(root)
    print_inorder_successor(root)

if __name__ == '__main__':
    test_inorder_successor()

# Output:
# Printing inorder successors using next pointer
# 3 -> 8
# 8 -> 10
# 10 -> 12
# 12 -> None
