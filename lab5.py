# Лабораторная работа №5
import random

# Задача 1
print("Пустой список:")
students = []
print(students)

n = int(input("Введите количество учащихся: "))
for i in range(0, n, 1):
    students.append(input("Резюме: "))
print("Полный список:")
for i in range(0, n, 1):
    print(students[i])

p = int(input("Введите индекс элемента, который необходимо удалить: "))
students.pop(p)
n = n - 1
print("Удаление элемента:")
for i in range(0, n, 1):
    print(students[i])

j = int(input("Введите индекс элемента, куда необходимо вставить элемент: "))
a = input("Введите сам элемент, который необходимо вставить: ")
n = n + 1
students.insert(j, a)
print("Добавление элемента:")
for i in range(0, n, 1):
    print(students[i])

print("Перевернутый список:")
students.reverse()
for i in range(0, n, 1):
    print(students[i])

print("Список после очищения:")
students.clear()
print(students)

# Задача 2.1
people = []
n = int(input("Введите количество учащихся: "))
for i in range(1, n + 1, 1):
    people.append(input("ФИО: "))
    people.append(input("Секция: "))

print("Сортировка по дисциплинам:")
for i in range(1, n, 1):
    for j in range(1, ((n - 1) * 2 - (i - 1) * 2), 2):
        if(people[j] > people[j + 2]):
            people[j], people[j + 2] = people[j + 2], people[j]
            people[j - 1], people[j + 1] = people[j + 1], people[j - 1]
for i in range(0, n * 2, 2):
    print(people[i] + ' ---> ' + people[i + 1])

print("Сортировка по ФИО:")
for i in range(1, n, 1):
    for j in range(1, ((n - 1) * 2 - (i - 1) * 2), 2):
        if(people[j - 1] > people[j + 1]):
            people[j], people[j + 2] = people[j + 2], people[j]
            people[j - 1], people[j + 1] = people[j + 1], people[j - 1]
for i in range(0, n * 2, 2):
    print(people[i] + ' ---> ' + people[i + 1])

# Задача 2.2
pupils = ["Alla", 4.7, "Aina", 5.0, "Batyr", 3.9, "Anton", 4.2]
x = 0
while(True):
    x = input()
    if(x == "."):
        break
    for i in range(0, len(pupils), 1):
        if(pupils[i] == x):
            print(pupils[i + 1])

# Задачи 2.3 - 2.4
mylist = []
x = 0
while(True):
    x = int(input())
    if(x == 0):
        break
    mylist.append(x)
for i in range(1, len(mylist), 1):
    for j in range(0, (len(mylist) - 1 - (i - 1)), 1):
        if(mylist[j] > mylist[j + 1]):
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
print("Список:")
for i in range(0, len(mylist), 1):
    print(mylist[i])
mylist.reverse()
print("Список:")
for i in range(0, len(mylist), 1):
    print(mylist[i])

# Задачи 2.5
lucky = []
for i in range(0, 6, 1):
    lucky.append(random.randint(1, 1))
print("Lucky ticket:")
print(lucky)

print("Generate:")
gen = []
k = 0
while(True):
    for i in range(0, 6, 1):
        gen.append(random.randint(1, 1))
    k = k + 1
    print(gen)
    if(gen == lucky):
        break
    gen.clear()
print("Result: " + str(gen))
print("Number of try: " + str(k))

# Задачи 2.6
def sort_or_not(list):
    result = False
    new_list = sorted(list)
    if(list == new_list):
        result = True
    new_list.reverse()
    if(list == new_list):
        result = True
    return result
the_list = []
c = int(input("Введите количество элементов в списке: "))
for i in range(0, c, 1):
    the_list.append(int(input()))
print(sort_or_not(the_list))