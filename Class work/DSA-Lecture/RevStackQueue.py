class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


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

class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            poped_data = temp.data
            self.top = self.top.next
            temp = None
            return poped_data

    def print(self):
        temp = self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp = temp.next

def reverse_stack(s1):
    q1 = Queue()
    while not s1.isempty():    #pop from stack and enqueue in queue
        q1.enqueue(Node(s1.pop()))
    q1.print()


que = Queue()
que.enqueue(Node(20))
que.enqueue(Node(30))
que.enqueue(Node(40))
que.enqueue(Node(50))
que.enqueue(Node(60))
que.print()



st = stack()

st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))
st.push(Node(90))

st.print()


st.pop()
st.print()

st.reverseString("PRASAD")
