balance = 10000
try:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise Exception("Insufficient Balance")
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)