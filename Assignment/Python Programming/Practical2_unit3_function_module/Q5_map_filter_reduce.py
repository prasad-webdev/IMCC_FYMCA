# Q5. Map, Filter and Reduce 
# Given:
# numbers = [1,2,3,4,5,6,7,8,9,10]
# Perform the following operations:
# 1. Use map() to generate squares of all numbers.
# 2. Use filter() to extract even numbers.
# 3. Use reduce() to calculate the sum of all numbers.
# Display all results.


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x * x, numbers))         # Generate squares using map()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))         # Extract even numbers using filter()
total = reduce(lambda x, y: x + y, numbers)          # Calculate sum using reduce()
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Sum:", total)
