# Лабораторная работа №4

# Задача 1
s1 = (input("Введите первую строку: "))
s2 = (input("Введите вторую строку: "))
print('Конкатенация строк:\n' + s1 + s2)
print('Повторение первой строки два раза:\n' + s1 * 2)
print('Обращение по отрицательному индексу первой строки:\n' + s1[-1])
print('Извлечение среза из второй строки:\n' + s2[1:8:3])
print('Длина строки:\n' + str(len(s1)))
print('Состоит ли строка только из чисел?\n' + str(s1.isdigit()))
print('Состоит ли строка только из букв?\n' + str(s1.isalpha()))
print('Состоит ли строка только из символов в нижнем регистре?\n' + str(s2.islower()))
print('Состоит ли строка только из символов в верхнем регистре?\n' + str(s2.isupper()))
print('Преобразование строки к нижнему регистру:\n' + s2.lower())
print('Преобразование строки к верхнему регистру:\n' + s2.upper())

# Задача 2
students = []
n = int(input("Введите количество учащихся: "))
for i in range(1, n + 1, 1):
    students.append(input("ФИО: "))
    students.append(input("Класс: "))
for i in range(1, n, 1):
    for j in range(1, ((n - 1) * 2 - (i - 1) * 2), 2):
        if(int(students[j]) > int(students[j + 2])):
            students[j], students[j + 2] = students[j + 2], students[j]
            students[j - 1], students[j + 1] = students[j + 1], students[j - 1]
for i in range(0, n * 2, 2):
    print(students[i] + ' ---> ' + students[i + 1])

# Задача 3.1
s = input("Введите строку: ")
sum = 0
for i in range(0, len(s), 1):
    sum = sum + int(s[i].isupper())
if(len(s) - 2 * sum >= 0):
    s = s.lower()
else:
    s = s.upper()
print(s)

# Задача 3.2
while(True):
    a = input("Введите первое целое число: ")
    b = input("Введите второе целое число: ")
    if(a.isdigit() and b.isdigit()):
        a = int(a)
        b = int(b)
        break
    else:
        print("Вы не ввели два целых числа!")
print(a + b)