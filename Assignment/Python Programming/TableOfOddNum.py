# print the table of odd no from 1-10
for num in range(1, 11):
    if num % 2 != 0:
        print("Table of", num)
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)
        print()