# EX 1

# def greet():
#     name = input("EX 1: Enter your name!: ")
#     print(f"EX 1: Hello, {name}!")
# greet()

# EX 2

# def add(a,b):
#     res = a + b
#     print(f"EX 2: {res}")
# add(5,5)

# EX 3

# def is_even(n):
#     if n % 2 == 0:
#         print(f"EX 5: True")
#     else:
#         print(f"EX 5: False")

# num = int(input(f"EX 5: Enter any number: "))
# is_even(num)

# EX 4

# def factorial(n):
#     f = 1
#     for i in range(2, n+1):
#         f *= i
#     return f

# num = int(input(f"EX 4: Enter any number: "))
# res = factorial(num)
# print(f"EX 4: Factorial of {num} is {res}")

# EX 5

# def find_max(a,b,c):
#     print(f"{max(a,b,c)}")

# a_i = int(input(f"EX 5: Enter a number (a): "))
# b_i = int(input(f"EX 5: Enter a number (b): "))
# c_i = int(input(f"EX 5: Enter a number (c): "))

# find_max(a_i,b_i,c_i)

# EX 6

def power(base, exp):
    return base ** exp

num1 = int(input(f"EX 6: Enter first number: "))
num2 = int(input(f"EX 6: Enter second number: "))

res = power(num1, num2)
print(f"EX 6: {num1} ** {num2} = {res}")

# EX 7

