class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

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
            print("Popped element: ", temp.data)
            self.top = self.top.next



            temp = None

    def display(self):
        temp = self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp = temp.next

    def reverseString(self, string):
        st1 = stack()

        for ch in string:
            st1.push(Node(ch))

        result = ""
        while not st1.isempty():
            result = result + st1.top.data
            st1.top = st1.top.next

        print("Reversed String: ", result)

    def reverse(self):
        st1 = stack()
        temp = self.top

        while temp:
            st1.push(Node(temp.data))
            temp = temp.next

        return st1

st = stack()

st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))
st.push(Node(90))

st.display()


st.pop()
st.display()

st.reverseString("PRASAD")

st1 = st.reverse()
print("Reversed Stack...")
st1.display()
