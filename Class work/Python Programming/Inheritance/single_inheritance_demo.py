class Parent:
    def parentsMethod(self):
        print("This is a method in the Parent class.")

class Child(Parent):
    def childMethod(self):
        print("This is a method in the Child class.")

# Create an instance of the Child class
c = Child()
c.parentsMethod()  # This will print: "This is a method in the Parent class."
c.childMethod()    # This will print: "This is a method in the Child class."