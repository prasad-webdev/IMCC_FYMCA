# # sentence = input("Enter your string : ")
# # vowels = "aeiouAEIOU"
# # count = 0

# # for char in sentence:
# #     if char in vowels:
# #         count += 1  
# # print("Total vowels:", count)

# txt = 'ha'
# print(txt*3)

# str = "prasad"
# print("Letter a Occurs", str.count("a"), "times in text")
# print(str.replace("a", "z"))
# print(str.split())

# mid = len(str) // 2
# part1 = str[:mid]   
# part2 = str[mid:]   
# print("First part :", part1)
# print("Second part:", part2)

# sort = sorted(str)
# print(sort)

# sorted("Pranav")

# my_list = []
# print(my_list)

# fruits = ["apple","banana","cherry"]
# print(fruits)

# numbers = [10,20,30,40]
# print(numbers[0])
# print(numbers[-2])

# colors = ["red","blue"]
# # colors.append("green")
# # print("after appending at last ",colors)

# # colors.insert(1, "yellow")
# # print("after insertion at second position",colors)

# print("before remove",colors)
# colors.pop()

# number = [1,2,3,4,5,6,7,8,9]
# print(len(number))
# print(sum(number))
# print("Ascending order",sorted(number))
# print("Descending order",sorted(number, reverse = True))

#create a list of 10 number and display the sum of last four elements
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
last_four = numbers[-4:]
total = sum(last_four)
print("Last four elements:", last_four)
print("Sum of last four elements:", total)


#remove the items at from the list located at second and fifth position
removed_fifth = numbers.pop(4)
removed_second = numbers.pop(1)
print("Removed: ",removed_second ,"and", removed_fifth)
print("Updated list:", numbers)


#print deff of highest and lowest number

highest = max(numbers)
lowest = min(numbers)
difference = highest - lowest
print("Highest number:", highest)
print("Lowest number :", lowest)
print("Difference    :", difference)

#append new element in list which is half of the item of located in the 3rd and 5th postion
third_item = numbers[2]
half_val = third_item / 2
numbers.append(half_val)
print("Original 3rd item:", third_item)
print("Updated list:", numbers)