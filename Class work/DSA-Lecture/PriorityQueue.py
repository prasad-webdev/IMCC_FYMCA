class node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_node):
        if self.front is None:        #first node to be inserted
            self.front = self.rear = new_node
            return

        if self.front.priority > new_node.priority:  #first position   
            new_node.next = self.front
            self.front = new_node
            return
        else:
            temp = self.front
            while temp.next:
                if new_node.priority < temp.next.priority:
                    break
                else:
                    temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

            if new_node.next is None:
                self.rear = new_node

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

#create priority queue 

pq = PriorityQueue()
pq.enqueue(node(100, 2))
pq.enqueue(node(500, 6))
pq.enqueue(node(300, 3))
pq.enqueue(node(700, 1))
pq.enqueue(node(400, 7))

pq.display()
