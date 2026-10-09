# n=int(input("enter a number : "))
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n%2==0:
#             return False
#     return True
# if is_prime(n):
#     print(n,"the number is prime")
# else:
#     print(n,"the number is not prime")

num=int(input("enter number : "))
flag = 0
for i in range(2,(num//2)+1):
    if (num%i==0):
        flag = 1
        break
if (flag == 1):
    print("number is not prime")
else:
    print("number is prime")