# n = int(input("enter a number = "))
# num = abs(n)
# total = 0
# while num > 0:
#     total = total + num % 10
#     num //= 10
# print("Sum of digits of is: ",total)

# num = int(input("enter a number : "))
# sum = 0
# while(n > 0):
#     sum = sum + (num%10)
#     n = num // 10
# print("sum of digit is : ",sum)

num = int(input("enter a number : "))
sum = 0
n = num
while(n > 0):
    sum = sum*10 + (n%10) 
    n = num // 10
if  (num==sum): 
    print("palindrome")