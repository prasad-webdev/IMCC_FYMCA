# Q3. Math and Random Module 
# Write a program that:
# • Generates a random number between 1 and 100.
# • Finds its square root using the math module.


import random
import math
num = random.randint(1, 100)    #Generates random number
result = math.sqrt(num)
print("Random Number:", num)
print("Square Root:", result)
