# Single Linear Linked List
# Ass1: Create a Singly Linear Linked List with following operations

# Create Linked List
# Traverse and print the node values
# Insert node at a specific position
# Find Middle node and print its value
# Delete node
# Reverse list
# Calculate the sum of every two consecutive node values.


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create / Append
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # 2. Traverse and print
    def print(self):
        temp = self.head
        count = 0
        total_sum = 0
        nodes = []
        while temp:
            nodes.append(str(temp.data))
            count += 1
            total_sum += temp.data
            temp = temp.next
        print(" -> ".join(nodes) if nodes else "List is empty")
        print(f"Total number of nodes: {count}")
        print(f"Sum of node values: {total_sum}")

    # 3. Insert node at a specific position 
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position!")
            return
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1
        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Position out of bounds!")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find middle node and print its value 
    def find_middle(self):
        temp = temp1 = self.head
        prev = None
        while temp1 and temp1.next:
            prev = temp
            temp = temp.next
            temp1 = temp1.next.next
        print("Middle node value:", temp.data)
        prev.next = temp.next
        temp = None

    # 8. Delete middle node
    def delfirst_last(self):
        temp1 = self.head
        temp1 = None
        prev = None
        temp = self.head = self.head.next
        while(temp.next):
            prev = temp
            temp = temp.next
        prev.next = None
        temp = None

        # 9. Delete alternate nodes (deletes 2nd, 4th, 6th, etc.)
    def delete_alternate(self):
        if not self.head or not self.head.next:
            return  
        curr = self.head
        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next

    # 5. Delete node by value
    def delete(self, val):
        if not self.head:
            print("List is empty")
            return

        # If head holds the value
        if self.head.data == val:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.data != val:
            temp = temp.next

        if temp.next is None:
            print(f"Node with value {val} not found")
            return

        temp.next = temp.next.next

    # 6. Reverse list in-place
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # 7. Calculate sum of every two consecutive node values
    def sum_consecutive_pairs(self):
        if not self.head or not self.head.next:
            print("Not enough nodes to form consecutive pairs")
            return []

        temp = self.head
        pair_sums = []
        while temp.next:
            pair_sums.append(temp.data + temp.next.data)
            temp = temp.next

        print("Sum of consecutive pairs:", pair_sums)
        return pair_sums


def solution():
    ll = LinkedList()

    # 1. Create list
    ll.append(Node(10))
    ll.append(Node(20))
    ll.append(Node(30))
    ll.append(Node(55))
    ll.append(Node(48))

    # 2. Traverse and print
    print("--- Initial List ---")
    ll.print()

    # 3. Insert at position
    print("\n--- Insert 100 at pos 1 ---")
    ll.insert(Node(100), 1)
    ll.print()

    # 4. Find middle node
    print("\n--- Middle Node ---")
    ll.find_middle()

    # 5. Delete node
    print("\n--- Delete Node 30 ---")
    ll.delete(30)
    ll.print()

    # 6. Reverse list
    print("\n--- Reverse List ---")
    ll.reverse()
    ll.print()

    # 7. Sum of consecutive nodes
    print("\n--- Consecutive Pair Sums ---")
    ll.sum_consecutive_pairs()
    # 8. Delete alternate nodes
    print("\n--- Delete Alternate Nodes ---")
    ll.delete_alternate()
    ll.print()


if __name__ == "__main__":
    solution()