# Q2. Lambda Function
# Create a lambda function to calculate the square of a number.
# # Accept a number from the user and display its square.

square = lambda num: num * num               # Lambda function to calculate square
num = int(input("Enter a number: "))
print("Square =", square(num))