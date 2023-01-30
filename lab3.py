# Лабораторная работа №3

import random
# Задача 1
a = int(input("Введите целое число: "))
while(a > 0):
    print(a)
    a = a - 1

# Задача 2
print("Использование range() для создания списка:")
mylist = list(range(7))
mylist.append("text")
print(mylist)

# Задача 3
print("Случайные числа: ")
print(random.randint(0, 1))
print(random.randrange(0, 1))
print(random.random())
for i in enumerate(mylist):
    print(i)

# Задача 4.1
a = int(input("Введите целое число: "))
b = int(input("Введите другое целое число, которое больше или равно предыдущему: "))
print("Результат:")
for i in range(a, b + 1):
    print(i)

# Задача 4.2
x = int(input("Введите целое число: "))
y = int(input("Введите другое целое число: "))
print("Результат:")
if(x < y):
    for i in range(x, y + 1, 1):
        print(i)
elif(x > y):
    for i in range(x, y - 1, -1):
        print(i)
else:
    print(x)

# Задача 4.3
k = int(input("Введите целое число: "))
l = int(input("Введите другое целое число, которое меньше предыдущего: "))
print("Результат:")
for i in range(k - (k % 2 == 0), l - 1, -2):
        print(i)

# Задача 4.4
n = int(input("Введите число карточек: "))
sum = 0
print("Введите номера карточек от 1 до n: ")
for i in range(1, n + 1, 1):
    sum = sum + i
for i in range(n - 1, 0, -1):
    sum = sum - int(input())
print("Номер потерянной карточки: " + str(sum))
