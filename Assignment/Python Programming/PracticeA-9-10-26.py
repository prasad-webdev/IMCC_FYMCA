# 1. print the table of odd no from 1-10
for num in range(1, 11):
    if num % 2 != 0:
        print("Table of", num)
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)
        print()

# 2. create a heterogeneous list of numbers and names. Split the list from highest numbers

heterogeneous_list = [1, "Ajay", 2, 3, 5, "Seema", "Anita"]
heterogeneous_list.append("Prasad")
heterogeneous_list[3:3] = [6, 7]
numbers = [x for x in heterogeneous_list if isinstance(x, (int, float))]
highest_num = max(numbers)
split_index = heterogeneous_list.index(highest_num)
part1 = heterogeneous_list[:split_index]
part2 = heterogeneous_list[split_index:]
print(part1, part2)


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

# 6. add the two numbers at third position of the list and append one name in the list and split.
heterogeneous_list = [1, "Ajay", 2, 3, 5, "Seema", "Anita"]
heterogeneous_list.append("Prasad")
heterogeneous_list[3:3] = [6, 7]
numbers = [x for x in heterogeneous_list if isinstance(x, (int, float))]
highest_num = max(numbers)
split_index = heterogeneous_list.index(highest_num)
part1 = heterogeneous_list[:split_index]
part2 = heterogeneous_list[split_index:]
print(part1, part2)