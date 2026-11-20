# Q6. Decorator Implementation 
# Create a decorator named execution_time() that:
# Displays a message before function execution.
# Executes the function.
# Displays a message after function execution.
# Apply this decorator to a function that calculates the factorial of a number.


def execution_time(func):       # Decorator function
    def wrapper():
        print("Function Started")
        func()
        print("Function Finished")
    return wrapper

@execution_time           # Apply decorator
def factorial():
    num = 5
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial =", fact)
factorial()
