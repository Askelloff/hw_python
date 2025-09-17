# ---Practice-lesson04---

# 1

# list_num = [1,2,3,4,5,6,7,8,9,10]

# print(list_num[::-1])

# 2

# list_names = ["Noah", "Oliver", "Liam", "Ethan", "Mason", "Olivia"]

# delete = -1

# print(f"Deleted ({list_names[delete]})")
# list_names.pop(delete)
# list_names.extend(["Petrov", "Ivanov"])
# print(f"Added ({list_names[-1]}, {list_names[-1]})")
# print(list_names)

# 3

# text_input = input("Enter any word: ")

# for i in (text_input):
#     print(i)

# 4

# list_num = [1,2,3,4,5,6,7,8,9,10]

# i = 1
# for i in (list_num):
#     if i % 2 == 0:
#         list_num.remove(i)
# print(list_num)
    
# 5

# list_num = [1,1,2,2,3,4,5,6,6,7,8,8,9,10,10]

# new_list_num = []
# for i in list_num:
#     if i not in new_list_num :
#         new_list_num.append(i)

# print(new_list_num)

# 6

# numbers = []
# squared = []
# cubed = []

# for i in range(1, 11):
#     numbers.append(i)
#     squared.append(i ** 2)
#     cubed.append(i ** 3)

# print(numbers)
# print(squared)
# print(cubed)

# 7

# total = sum(range(1, 101))
# print(total)

# 8

# numbers = [1,50,2,3,14,25,5,6,1,2,64]

# for i in numbers[:]:
#     if i <= 10:
#         numbers.remove(i)
# print(numbers)

# 9

# num = ""
# while num != 0:
#     num = int(input("Enter 0: "))
# print("You entered 0!")

# 10

# num = []

# for i in range(1, 11):
#     num.append(i ** 2)
# print(num)

# 11

# n = int(input("Enter any number: "))
# fact = 1

# for i in range(1, n+1):
#     fact *= i
# print(fact)

# 12

# num = int(input("Enter any number: "))

# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")

# ---Practice-lesson05---

# 1

# num = [i for i in range(1,21) if i % 3 == 0]
# print(num)

# 2

# num = [i ** 2 for i in range(1,11) if i % 2 == 0]
# print(num)

# 3

# fruits_list = ["apple", "banana", "cherry"]

# fruits = [i[0] for i in fruits_list]
# print(fruits)

# 4

# mult_tab = [[i * j for i in range(1,6)] for j in range(1,6)]

# for row in mult_tab:
#     print(row)

# 5

# numbers = [5,6,-2,1,-5,2,3,8,-12,4,2,-13,6,-1]

# n_num = [i for i in numbers if i <= 0]
# print(n_num)

# 6

# numbers = [3, -1, 7, 10, -5, 8, 2, -9, 6]
# words = ["яблоко", "груша", "банан", "апельсин", "слива", "черника"]

# ex1 = [sum(numbers)]
# print(f"EX1: {ex1}")

# ex2 = [max(numbers), min(numbers)]
# print(f"EX2: {ex2}")

# ex3 = sorted(numbers)
# ex3_5 = sorted(numbers, reverse=True)
# print(f"EX3: {ex3}\n     {ex3_5}")

# ex4 = [f"Min: {min(words, key=len)}", f"Max: {max(words, key=len)}"]
# print(f"EX4: {ex4}")

# ex5 = [all(num % 2 == 0 for num in numbers)]
# print(f"EX5: {ex5}")

# ex6 = [any(num % 2 == 0 for num in numbers)]
# print(f"EX6: {ex6}")

# ex7 = [sum(i for i in numbers if i >= 0)]
# print(f"EX7: {ex7}")

# ex8 = sorted(words, key=len)
# print(f"EX8: {ex8}")

# ---Exercise--- 

# 1

# num = [i ** 2 for i in range(1,21) if i % 2 == 0]
# print(num)

# 2

# words = ["Апельсин", "банан", "Авокадо", "Вишня", "ананас", "груша"]

# fruits = [i for i in words if i[0].isupper()]
# print(fruits)

# 3

# words = ["кот", "автомобиль", "река", "компьютер", "дом"]

# words1 = [i for i in words if len(i) > 5]
# print(words1)

# 4

# numbers = [1, 3, 5, 9, 12, 15, 18, 20]

# numbers1 = [i **3 for i in numbers if i % 3 == 0]
# print(numbers1)

# 1.1

# with open("numbers.txt", "w", encoding="UTF-8") as f:
#     for i in range(1, 51):
#         f.write(f"{i}\n") 

# 2.1

# words = ["яблоко", "груша", "кот", "авто", "дверь", "окно"]

# with open("words.txt", "w", encoding="UTF-8") as f:
#     for i in words:
#         if (len(i) < 5):
#             f.write(f"{i}\n")

# 3.1

# with open("input.txt", "r", encoding="UTF-8") as f:
#     lines = f.readlines()

# lines.reverse()

# with open("reversed.txt", "w", encoding="UTF-8") as f:
#     f.writelines(lines)
    