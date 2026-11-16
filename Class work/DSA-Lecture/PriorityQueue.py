class node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None

class priorityQueue:
    def _init__(self):
        self.front = self, rear = None

    def enqueue(self, new_node):
        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return
        else:
            temp = self.front
            while temp.next:
                if new_node.priority <= temp.priority:
                    break
                else:
                    prev = temp
                    temp = temp.next
            prev.next = new_node
            new_node.next = temp






    def dequeue(self):



