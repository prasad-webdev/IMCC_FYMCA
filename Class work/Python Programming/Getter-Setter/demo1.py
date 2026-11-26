class student:


    def __init__(self):
        self.__name = ""
        self.__rollno = None
        self.__marks = None 


    def set_data(self, name, rollno, marks):
        self.__name = name
        self.__rollno = rollno

        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")


    def get_data(self):
        print("Name:", self.__name
              , "Roll No:", self.__rollno
              , "Marks:", self.__marks)

s1 = student()
name = input("Enter name: ")
rollno = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))

s1.set_data(name, rollno, marks)
print("Student details:")
s1.get_data()
