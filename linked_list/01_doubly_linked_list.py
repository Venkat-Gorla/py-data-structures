
# given a doubly linked list (dll), reverse it
# reversing a dll is different and actually simpler compared to sll, let's see how to do it

class Node:
    """
    A class representing a node in a doubly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    A class representing a doubly linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Add a node to the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_fwd(self):
        """
        Print the list from head to tail.
        """
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

    # solution code: 
    # in-place reverse method
    def reverse(self):
        # for every node, just swap the next and prev pointers
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev

        # swap head and tail
        self.head, self.tail = self.tail, self.head

def main():
    dll = DoublyLinkedList()
    for i in range(1, 6):
        dll.append(i)

    print("Original list:")
    dll.print_fwd()

    # reversing the list
    dll.reverse()

    print("Reversed list:")
    dll.print_fwd()

if __name__ == "__main__":
    main()

# output
# Original list:
# 1 <-> 2 <-> 3 <-> 4 <-> 5
# Reversed list:
# 5 <-> 4 <-> 3 <-> 2 <-> 1

