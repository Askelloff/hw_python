# E1

# cost1 = int(input("Enter any cost:"))

# if cost1 <= 1000:
#     print(f"without discount\nprice: {cost1}")
# elif cost1 >= 1000 and cost1 <= 5000:
#     print(f"discount 5%\nprice: {cost1 - (cost1 * 5 / 100)}")
# elif cost1 >= 5000 and cost1 <= 10000:
#     print(f"discount 10%\nprice: {cost1 - (cost1 * 10 / 100)}")
# elif cost1 >= 10000:
#     print(f"discount 15%\nprice: {cost1 - (cost1 * 15 / 100)}")

# E2

# time1 = int(input("Enter the time (0 - 23):"))

# if time1 >= 0 and time1 <= 5:
#     print(f"night")
# elif time1 >= 6 and time1 <= 11:
#     print(f"morning")
# elif time1 >= 12 and time1 <= 17:
#     print(f"day")
# elif time1 >= 18 and time1 <= 23:
#     print(f"evening")
# else:
#     print("ERROR")

# E3

# year1 = int(input("Enter any year:"))

# if (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0):
#     print(f"Leap year")
# else:
#     print(f"Not leap year")

# E4

# shape1 = input("Choose a shape (circle, triangle, rectangle):")

# if shape1 == 'circle':
#     r = int(input("Enter radius of circle:"))
#     pi = 3.14
#     area = pi * r ** 2
#     print(f"area of circle is :{area}")
# elif shape1 == 'rectangle':
#     h = int(input("Enter height of rectangle:"))
#     w = int(input("Enter width of rectangle:"))
#     area = h * w
#     print(f"area of rectangle is :{area}")
# elif shape1 == 'triangle':
#     a = int(input("Enter base length of triangle:"))
#     h = int(input("Enter height of rectangle:"))
#     area = 0.5 * h * a
#     print(f"area of rectangle is :{area}")
# else:
#     print(f"ERROR")

# E5

# correct_password = "Secret123"
# attempts = 0
# max_attempts = 3

# while attempts < max_attempts:
#     password = input("Enter password: ")
#     if password == correct_password:
#         print(f"Welcome back!")
#         break
#     else:
#         attempts += 1
#         print(f"Try again")
# else: 
#     print(f"Access denied. Too many attempts.")

# E6

# money1 = int(input("Enter any amount in USD$: "))

# currency1 = input("Enter any  currency (EUR, CZK, GBP): ").upper()
# if currency1 == "EUR":
#     result = money1 * 0.85
#     print(f"{result}€")
# elif currency1 == "CZK":
#     result = money1 * 20.8
#     print(f"{result}Kč")
# elif currency1 == "GBP":
#     result = money1 * 0.74
#     print(f"{result}£")
# else:
#     print(f"ERROR")

# E7

# month = int(input("Enter any month (1-12): "))

# match month:
#     case 1:
#         print(f"31")
#     case 2:
#         print(f"28")
#     case 3:
#         print(f"31")
#     case 4:
#         print(f"30")
#     case 5:
#         print(f"31")
#     case 6:
#         print(f"30")
#     case 7:
#         print(f"31")
#     case 8:
#         print(f"31")
#     case 9:
#         print(f"30")
#     case 10:
#         print(f"31")
#     case 11:
#         print(f"30")
#     case 12:
#         print(f"31")

#  Practice 

# 1

# login = "admin"
# password = "12345"

# login_input = input("Enter login: ")
# password_input = input("Enter password: ")

# if login == login_input and password == password_input:
#     print(f"Welcome back!")
# elif login != login_input:
#     print(f"incorrect login.")
# elif password != password_input:
#     print(f"incorrect password.")

# 2

# number = int(input("Enter any number: "))

# if number % 3 == 0 and  number % 5 != 0:
#     print(f"The number is divisible by 3 = {number // 3}")
# elif number % 5 == 0 and number % 3 != 0:
#     print(f"The number is divisible by 5 = {number // 5}")
# elif number % 3 == 0 and number % 5 == 0:
#     print(f"The number is divisible by 3 and 5:\n{number} : 3 = {number // 3}\n{number} : 5 = {number // 5}")
# elif number % 3 != 0 and number % 5 != 0:
#     print(f"The number is not divisible by 3 and 5")

# 3

# month = int(input("Enter any month (1-12): "))

# match month:
#     case 12|1|2:
#         print(f"It's winter")
#     case 3|4|5:
#         print(f"It's spring")
#     case 6|7|8:
#         print(f"It's summer")
#     case 9|10|11:
#         print(f"It's autumn")
#     case _:
#         print(f"Invalid month number!")

# 4

# age = int(input("Enter your age: "))

# if age >= 0 and age <= 12:
#     print(f"You are a child")
# elif age >= 13 and age <= 17:
#     print(f"You are a teenager")
# elif age >= 18 and age <= 64:
#     print(f"You are a adult")
# elif age >= 65:
#     print(f"You are a senior")

# 5

# number = int(input("Enter any number: "))

# if number % 2 == 0:
#     print(f"is even")
# else:
#     print(f"is odd")

# 6

# password = "PythonRocks"
# password_input = input("Enter password: ")

# if password == password_input:
#     print(f"Welcome back!")
# else:
#     print(f"Invalid password")

# 7

# day_of_week = int(input("Enter any day of the week (1-7): "))

# match day_of_week:
#     case 1:
#         print(f"Monday")
#     case 2:
#         print(f"Tuesday")
#     case 3:
#         print(f"Wednesday")
#     case 4:
#         print(f"Thursday")
#     case 5:
#         print(f"Friday")
#     case 6|7:
#         print(f"Weekend")
#     case _:
#         print(f"Incorrect day of the week!")