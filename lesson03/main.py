# E1

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     op_input = input("Enter any arithmetic operatot (+, -, *, /): ")
#     match op_input:
#         case "+":
#             print(f"{num1} + {num2} = {num1 + num2}")
#         case "-":
#             print(f"{num1} - {num2} = {num1 - num2}")
#         case "*":
#             print(f"{num1} * {num2} = {num1 * num2}")
#         case "/":
#             print(f"{num1} / {num2} = {num1 / num2}")
#         case _:
#             print("Invalid operator!")
# except ValueError:
#     print("This is not a number.")
# except ZeroDivisionError:
#     print("Сannot be divided by zero.")


# Practice

# 1

# num1 = 5
# num2 = 0

# try:
#     print(f"{num1 / num2}")
# except ZeroDivisionError:
#     print("cannot be divided by zero.")

# 2

# while True:
#     try:
#         number = int(input("Enter any number or digit: "))
#     except ValueError:
#         print("It's not a number. Try again: ")
#     else:
#         print(f"You entered the number: {number}!")
#         break

# 3

# try:
#     number = int(input("Enter the number: "))
#     divisior = int(input("Enter the divisior: "))
#     if number % divisior == 0: 
#         result = number // divisior
#         print(f"{result}")
#     elif number % divisior != 0:
#          result = number / divisior
#          print(f"{result}")
# except ValueError:
#     print("This is not a number.")
# except ZeroDivisionError:
#     print("Сannot be divided by zero.")

# 4

# try:
#     number = int(input("Enter any number or digit: "))
# except ValueError:
#     print("It's not a number. Try again")
# else:
#     print(f"You entered the number: {number}!")
# finally:
#     print("Program finished.")