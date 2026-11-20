# Q1. Function Scope and Built-in Functions 
# Write a function analyze_numbers() that accepts a list of numbers and displays:
# 1. Maximum value
# 2. Minimum value
# 3. Sum of all values
# 4. Average value
# Use Python built-in functions.

def analyze_numbers(numbers):
    print("Maximum =", max(numbers))
    print("Minimum =", min(numbers))
    print("Sum =", sum(numbers))
    print("Average =", sum(numbers) / len(numbers))
numbers = [10, 20, 30, 40]

analyze_numbers(numbers)