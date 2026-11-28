try:
    num = int(input("Enter number: "))
    try:
        result = 100 / num
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")