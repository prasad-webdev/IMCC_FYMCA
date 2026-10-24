class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
        return self.top is None
    
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            temp = self.top
            print('Poped Element :- ', temp.data)
            self.top = self.top.next
            temp = None
        
    def reversed(self):
        temp = self.top
        while(temp):
            st1.push(Node(temp.data))
            temp = temp.next
    def print(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            print('Stack Contains...')
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            
obj = Stack()
st1 = Stack()
obj.push(Node(1))
obj.push(Node(2))
obj.push(Node(3))
obj.push(Node(4))
obj.push(Node(5))