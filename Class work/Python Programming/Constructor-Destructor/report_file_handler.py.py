class Report:
    def __init__(self,filename):
        self.file = open(filename, 'w')
        print("Report created")

    def write_data(self, text):
        self.file.write(text)

    def __del__(self):
        self.file.close()
        print("Report destroyed")


r1 = Report("report.txt")
r1.write_data("This is the first line of the report.\n")



with open("report.txt", 'r') as f:
    print(f.read())

del r1