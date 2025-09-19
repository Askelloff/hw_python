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

# def power(base, exp):
#     return base ** exp

# num1 = int(input(f"EX 6: Enter first number: "))
# num2 = int(input(f"EX 6: Enter second number: "))

# res = power(num1, num2)
# print(f"EX 6: {num1} ** {num2} = {res}")

# EX 7

# def average(*numbers):
#     result = sum(numbers) / len(numbers)
#     return result
# print(f"EX 8: {average(1,2,3,4,5,6,7,8,9,10)}")

# EX 8

# def is_palindrome(word):
#     reverse = word[::-1]
#     if reverse == word:
#         print(f"EX 8: {reverse}")
#     else:
#         print(f"EX 8: This not a palindrome!")
# w_i = input(f"EX 8: Enter any word for test on palindrome: ")
# is_palindrome(w_i)

# EX 9

# import math

# def is_fibonacci(n):
#     def is_perfect_square(x):
#         s = int(math.isqrt(x))
#         return s * s == x
    
#     return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

# print(is_fibonacci(6))

# EX 10

def squares(n):
    num_list = []
    for i in range(1,n):
        return i**2
    print()
