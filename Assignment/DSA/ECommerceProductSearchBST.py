class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0
        self.lcnt = 0
        self.nlcnt = 0

    def insert(self, new_node): 
        if self.root is None:    # BST is empty
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:    # left subtree
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:    # right subtree
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    def search(self, rt, val):
        if rt is None:
            return False
        if val == rt.data:
            return True
        elif val < rt.data:
            return self.search(rt.left, val)
        else:
            return self.search(rt.right, val)

    def findminmax(self):
        if self.root is None:
            print("\nTree is empty")
            return
        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMin: ", temp.data)

        temp = self.root
        while temp.right:
            temp = temp.right
        print("Max: ", temp.data)

    def del_node(self, rt, val):
        if rt is None:
            return
        if val < rt.data:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)
        else:
            if rt.left is None:    # node with right child only
                return rt.right
            if rt.right is None:    # node with left child only
                return rt.left

            # node has both left and right children
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt

    def get_successor(self, rt):
        temp = rt.right
        while temp.left is not None:
            temp = temp.left
        return temp


b1 = BST()

# Insert product IDs
b1.insert(Node(150))
b1.insert(Node(100))
b1.insert(Node(200))
b1.insert(Node(75))
b1.insert(Node(125))
b1.insert(Node(175))
b1.insert(Node(250))
b1.insert(Node(60))
b1.insert(Node(90))
b1.insert(Node(110))

# Display product IDs in ascending order
print("\nProduct IDs in ascending order: ")
b1.inorder(b1.root)

# Search product ID
val = int(input("\nEnter product ID to search: "))
if b1.search(b1.root, val):
    print("Product ID", val, "exists")
else:
    print("Product ID", val, "does not exist")

# Delete product ID
val = int(input("\nEnter product ID to delete: "))
b1.root = b1.del_node(b1.root, val)

print("\nAfter deletion: ")
b1.inorder(b1.root)

# Display traversals after deletion
print("\n\nInorder: ")
b1.inorder(b1.root)

print("\nPreorder: ")
b1.preorder(b1.root)

print("\nPostorder: ")
b1.postorder(b1.root)

# Find minimum and maximum product IDs
b1.findminmax()