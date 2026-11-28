try:
    num = int(input("Enter a number: "))
    result = 50 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Enter integer only.")
else:
    print("Result:", result)
finally:
    print("Thank you for using the program.")