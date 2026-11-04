class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        temp = self.top
        self.top = temp.next
        return temp.data


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, element):
        new_node = Node(element)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

    def display(self):
        temp = self.front


        print("Queue elements: ", end="")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def reverse(self):
        st = stack()
        temp = self.front


        while temp:
            st.push(temp.data)
            temp = temp.next

        newQueue = Queue()

        while st.top:
            newQueue.enqueue(st.pop())

        return newQueue

    def merge(self, q2):
        q3 = Queue()

        temp = self.front
        while temp:
            q3.enqueue(temp.data)
            temp = temp.next

        temp = q2.front
        while temp:
            q3.enqueue(temp.data)
            temp = temp.next

        return q3

    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None and temp2 is None:
            return True

        return False



q1 = Queue()

q1.enqueue('A')
q1.enqueue('B')
q1.enqueue('C')

print("First Queue: ")
q1.display()

print("Dequeue: ", q1.dequeue())
q1.display()

q3 = q1.reverse()
print("Reversed Queue: ")
q3.display()

q2 = Queue()

q2.enqueue('D')
q2.enqueue('E')


q2.enqueue('F')

print("Second Queue: ")
q2.display()

q4 = q1.merge(q2)
print("Merged Queue: ")
q4.display()


if q1.identical(q2):
    print("Both Queues are Identical")
else:
    print("Both Queues are Not Identical")