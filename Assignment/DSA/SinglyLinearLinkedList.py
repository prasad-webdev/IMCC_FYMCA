# Single Linear Linked List
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List - append
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # 2. Traverse and print the node values
    def print(self):
        temp = self.head
        if not temp:
            print("Linked List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3. Insert node at a specific position (1-based index)
    def insert(self, new_node, position):
        if position < 1:
            print("Invalid position")
            return
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        count = 1
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        if not temp:
            print("Position out of range")
            return
        new_node.next = temp.next
        temp.next = new_node

    # 4. Delete the nodes having negative values
    def delete_negative(self):
        while self.head and self.head.data < 0:
            self.head = self.head.next
        temp = self.head
        while temp and temp.next:
            if temp.next.data < 0:
                t = temp.next
                t = None
                temp.next = temp.next.next
            else:
                temp = temp.next


list = LinkedList()

list.append(Node(10))
list.append(Node(-5))
list.append(Node(20))
list.append(Node(-15))
list.append(Node(30))

print("Original Linked List:")
list.print()


print("\nInsert node at a specific position :")
list.insert(Node(99), 3)
list.print()


print("\nAfter deleting negative values:")
list.delete_negative()
list.print()