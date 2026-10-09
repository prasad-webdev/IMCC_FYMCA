# n = int(input("Enter a number: "))
# rev = 0
# while n > 0:
#     rev = (rev * 10) + (n % 10)
#     n = n // 10
# print(rev)

n=int(input("enter a numbers : "))
rev = 0
while n!=0:
    r=n%10
    n=n//10
    rev=rev*10+r
print(rev)