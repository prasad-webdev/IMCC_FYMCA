class student:
    count = 0
    def __init__(self, name):
        self.name = name
        student.count += 1
        print("Student created")

    def __del__(self):
        student.count -= 1
        print("Student destroyed")

    @classmethod
    def total_students(cls):
        print("Total students:", cls.count)


s1 = student("Alice")
s2 = student("Bob")
s3 = student("Charlie")

student.total_students()

del s2

student.total_students()
