# EX 1

def greet(name):
    return f"EX 1: Hello, {name}"
print(greet("Alex"))

# EX 2

def add(a,b):
    return f"EX 2: {a + b}"

print(add(5,5))

# EX 3

def is_even(n):
    if n % 2 == 0:
        return f"EX 3: {True}"
    else:
         return f"EX 3: {False}"

print(is_even(2))

# EX 4

def factorial(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f"EX 4: {f}"

print(factorial(4))

# EX 5

def find_max(a,b,c):
    return f"EX 5: {max(a,b,c)}"

a = 11
b = 90
c = 88

print(find_max(a,b,c))

# EX 6

def power(base, exp):
    return f"EX 6: {base} ** {exp} = {base ** exp}"

print(power(2, 3))

# EX 7

def average(*numbers):
    return f"EX 7: {sum(numbers) / len(numbers)}"
    
print(average(1,2,3,4,5,6,7,8,9,10))

# EX 8

def is_palindrome(word):
    reverse = word[::-1]
    if reverse == word:
        return f"EX 8: {reverse}"
    else:
        return f"EX 8: This not a palindrome!"
print(is_palindrome("AWS"))

# EX 9

import math

def is_fibonacci(n):
    def is_perfect_square(x):
        s = int(math.isqrt(x))
        return s * s == x
    
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

print(f"EX 9: {is_fibonacci(6)}")

# EX 10

def squares(n):
    return [i**2 for i in range(1, n+1)]

print(f"EX 10: {squares(5)}")

# EX 11

def filter_even(numbers):
    return f"EX 11: {[i for i in numbers if i % 2 == 0 ]}"

print(filter_even([1,2,3,4,5,6,7,8]))

# EX 12

def sum_numbers(*args):
    return f"EX 12: {sum(args)}"

print(sum_numbers(1,2,3,4,5,6,7,8,9,10))

# EX 13

info_person = {
    "name" : "Ivan",
    "age" : 31,
    "city" : "Plzen"
} 

def print_person_info(**kwargs):
    return f"EX 13: Name: {kwargs["name"]}\n       Age: {kwargs["age"]}\n       City: {kwargs["city"]}"

print(print_person_info(**info_person))