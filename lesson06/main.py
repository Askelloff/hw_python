# ---Exercise---

# ---tuple---

# E1

print("---tuple---")

numbers = (2,22,1,31,52,46)

lst = list(numbers)
lst.append(99)
t = tuple(lst)
print(f"EX1: {t}")

# E2

words = ("cat","tree","planet","elephant","hippopotamus")

lst = list(words)
max_w = [max(lst, key=len)]
t = tuple(max_w)

print(f"EX2: {t}")

# E3

num1 = (2,6,7,8)
num2 = (4,3,1,5)

avg = sum(num1 + num2) / len(num1 + num2)

print(f"EX3: {avg}")

# E4

numbers = [1,2,3,4,5,6,7,8,9,10]

t = tuple(numbers)

if 10 in t:
    print(f"EX4: {10 in t}")
else:
    print(f"EX4: There is not 10")

# E5

words = ["cat tree planet elephant hippopotamus"]

w_lst = words[0].split()

t = tuple(w_lst)

print(f"EX5: {t[2]}")

# ---set---

print("---set---")

# E6

numbers = {1,6,54,7,8,46,41}
numbers.remove(6)
numbers.add(99)

print(f"EX6: {numbers}")

# E7

num1 = {1,3,5,4}
num2 = {2,1,3,4,5,6,7,5}

dbl = num1 & num2

print(f"EX7: {dbl}")

# E8

numbers = [1,2,5,4,6,8,2,4,6,5,8,4,2,1]

s = set(numbers)

print(f"EX8: {s}")

# E9

words = ["apple", "banana", "apple", "orange", "banana", "grape"]

uniq_words = set(words)
print(f"EX9: {uniq_words}")

# E10

X = {1, 2}
Y = {1, 2, 3, 4}

print(f"EX10: first list: {X.issubset(Y)}, second list: {Y.issubset(X)}")  

# ---dict---

print("---dict---")

# E11

students = {
    "John": 12,
    "Maria": 10,
    "Alex": 9,
}

students["Petro"] = 11
students["Alex"] = 13

print(f"EX11: {students}")

# E12

word = input("Enter any word: ")

char_cont = {}

for ch in word:
    if ch in char_cont:
        char_cont[ch] += 1
    else:
        char_cont[ch] = 1
print(f"EX12: {char_cont}")

# E13

name = ["John", "Mark", "Ilon", "Bart", "Alex"]
rating = [12,9,10,11,11]

students = {}

try:
    for i in range(len(name)):
        students.update({name[i] : rating[i]})
    print(f"EX13: {students}")
except IndexError:
    print("no index")

# E14

products = {
    "Iphone 16 pro": 1000,
    "BMW M5 F90 Competition": 49999
}

max_price = max(products, key=products.get)
print(f"EX14: {max_price}: {products[max_price]}$")

# E15

numbers = [1,2,3,4,5]

numbers1 = {}

for i in numbers:
    numbers1[i] = i**2
print(f"EX15: {numbers1}")

# E16

data = [("name", "iphone"), ("model","SE 2020"), ("ram", "256GB"), ("color", "Black")]

product = {}

for i in data:
    lst = list(i)
    product[lst[0]] = lst[1]
print(f"EX16: {product}")

# E17

numbers = {1,5,8,7,4,6,9,2,3}

s = set(numbers)

print(f"EX17: {min(s)}")

# E18

words = {"name", "iphone","model","SE 2020","RAM", "256GB","color", "Black"}

lst = list(words)

str = " ".join(lst)

print(f"EX18: {str}")

# E19

list1 = {
    "lst1": (21,46,82),
    "lst2": (43,51,45),
    "lst3": (84,13,5)
}

for key, value in list1.items():
    print(f"EX19: {key}: {max(value)}")

# E20

data1 = [("name", "iphone"), ("model","SE 2020"), ("ram", "256GB"), ("color", "Black")]

product = {}

for i in data1:
    lst = list(i)
    product[lst[0]] = lst[1]
print(f"EX20: {list(sorted(product.keys()))}")
