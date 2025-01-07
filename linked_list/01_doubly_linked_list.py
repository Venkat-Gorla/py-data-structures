
# given a doubly linked list (dll), reverse it
# reversing a dll is different and actually simpler compared to sll, let's see how to do it
# write code to swap pairs in the list,
# examples:
# 1<->2<->3 should become 2<->1<->3
# 1<->2<->3<->4 should become 2<->1<->4<->3

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

    # in-place reverse method
    def reverse(self):
        # for every node, just swap the next and prev pointers
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev

        # swap head and tail
        self.head, self.tail = self.tail, self.head

    def swap_pairs(self):
        # if list contains less than two elements, ignore
        if not (self.head and self.head.next):
            return

        current = self.head
        self.head = self.head.next # update head to the second node
        previous = None

        while current and current.next:
            next_node = current.next.next

            first = current
            second = current.next

            first.prev = second
            second.next = first
            second.prev = previous
            if previous:
                previous.next = second

            previous = first
            current = next_node
        # end while

        if current:
            # odd number of nodes
            current.prev = previous
            previous.next = current
            self.tail = current
        else:
            # even number of nodes
            previous.next = None # terminate list
            self.tail = previous

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, lst):
        for item in lst:
            self.append(item)

def test_swap_pairs():
    def build_and_swap(lst):
        dll = DoublyLinkedList()
        dll.from_list(lst)
        dll.swap_pairs()
        return dll.to_list()

    # Test cases
    assert build_and_swap([]) == []
    assert build_and_swap([1]) == [1]
    assert build_and_swap([1, 2]) == [2, 1]
    assert build_and_swap([1, 2, 3]) == [2, 1, 3]
    assert build_and_swap([1, 2, 3, 4]) == [2, 1, 4, 3]
    assert build_and_swap([1, 2, 3, 4, 5]) == [2, 1, 4, 3, 5]

def test_two_node_list():
    dll = DoublyLinkedList()
    dll.from_list([1, 2])
    dll.swap_pairs()
    assert dll.to_list() == [2, 1]
    assert dll.tail.data == 1 # Ensure tail is correctly updated
    assert dll.tail.next is None # Ensure the list terminates properly

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

    test_swap_pairs()
    test_two_node_list()
    print("\nAll test cases for swap_pairs passed.")

if __name__ == "__main__":
    main()

# output
# Original list:
# 1 <-> 2 <-> 3 <-> 4 <-> 5
# Reversed list:
# 5 <-> 4 <-> 3 <-> 2 <-> 1

# All test cases for swap_pairs passed.

