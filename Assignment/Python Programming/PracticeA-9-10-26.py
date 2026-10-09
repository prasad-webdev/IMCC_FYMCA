# 1. print the table of odd no from 1-10
for num in range(1, 11):
    if num % 2 != 0:
        print("Table of", num)
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)
        print()

# 2. create a heterogeneous list of numbers and names. Split the list from highest numbers

heterogeneous_list = [10, "Alice", 25, "Bob", 5, "Charlie", 30, "David"]
numbers = [x for x in heterogeneous_list if isinstance(x, (int, float))]
numbers.sort(reverse=True)
print("Numbers in descending order:", numbers)

# 3. accept the name and check if its palindrome.

name = input("Enter a name: ")
if name.lower() == name[::-1].lower():
    print(f"{name} is a palindrome.")
else:
    print(f"{name} is not a palindrome.")


# 4. print the sum of digits
num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print(total)


# 5. print the following pattern
# *
# ##
# ***

n = int(input("Enter the number of rows for the pattern: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print("*" * i)
    else:
        print("#" * i)

