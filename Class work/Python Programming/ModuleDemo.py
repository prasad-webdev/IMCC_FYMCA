# import mymodule as m
# m.greet_person("Alice")
# m.change_case("We are testing change case")




# def greet_person(name):
#     print("Hello", name + "!")

# def change_case(text):
#     result = ""
#     for ch in text:
#         if ch.isupper():
#             result += ch.lower()
#         elif ch.islower():
#             result += ch.upper()
#         else:
#             result += ch
#     return result

# greet_person("Alice")
# print(change_case("We are testing change case"))



# import math
# x = math.ceil(4.2)
# y = math.floor(4.8)

# print(x)
# print(y)

# print("factorial of 5 is", math.factorial(5))



# from module import greet_person
# greet_person("Alice")


# import random 
# x = random.randint(1, 100)
# subject = ("Math", "Science", "History", "Geography", "English", "Art", "Music", "Physical Education", "Computer Science", "Economics")
# mychoice = random.choice(subject)
# print(mychoice)
# print(x)


# import datetime
# print(datetime.date.today())
# print(datetime.datetime.now())
# print(datetime.timedelta(days=5))



from datetime import date, timedelta
now = datetime.now()
furture_date = now + timedelta(days=10)
past_date = now - timedelta(hours=5)

print("After 10 days, the date will be", furture_date)
print("5 hours ago, the date was", past_date)
