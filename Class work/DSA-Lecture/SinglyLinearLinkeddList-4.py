# Single Linear Linked List
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        # Case 1: Insert at beginning
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        # Case 2: Insert at any valid position
        temp = self.head
        p = 1

        while temp is not None and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Position is out of range. Node not inserted.")
            return

        new_node.next = temp.next
        temp.next = new_node

    def del_node(self, value):
        if self.head is None:
            print("List is empty")
            return

        # Delete first node
        if self.head.data == value:
            self.head = self.head.next
            return

        prev = self.head
        temp = self.head.next

        while temp is not None:
            if temp.data == value:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

        print("Value is not here in the list")

    def reverse_links(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def print(self):
        temp = self.head
        count = 0
        total_sum = 0
        while temp:
            print(temp.data, end=" -> ")
            count += 1
            total_sum += temp.data
            temp = temp.next
        print("None")
        print(f"Total number of nodes: {count}")
        print(f"Sum of node values: {total_sum}")
        print("-" * 30)


llist = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
llist.append(n1)
llist.append(n2)
llist.append(n3)
llist.append(Node(55))
llist.append(Node(48))

print("Initial List:")
llist.print()

print("Insert 100 at pos 1:")
llist.insert(Node(100), 1)
llist.print()

print("Insert 66 at pos 7:")
llist.insert(Node(66), 7)
llist.print()

print("Delete 30:")
llist.del_node(30)
llist.print()

print("Reverse the links of nodes:")
llist.reverse_links()
llist.print()