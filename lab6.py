# Лабораторная работа №6
import random

# Задача 1
my_tuple = (1, 2, 3, 4, 5, "aa", 5.6, "ab", "aa")
my_set = {6, 7, 8, 9, 10}
print(my_tuple.count("aa"))
print(my_tuple.index("aa", 6, 9))
my_set.add(6.99)
print(my_set)
my_set.pop()
print(my_set)
my_set.discard(6.99)
print(my_set)

# Задача 2.1

first_tuple = tuple(random.randint(0, 5) for i in range(0, 10))
second_tuple = tuple(random.randint(-5, 0) for i in range(0, 10))
third_tuple = first_tuple + second_tuple
print(third_tuple)
print(third_tuple.count(0))

# Задача 2.2

m_tuple = (7, (4.56, (5 + 7j, ("abc", ()))))
print(m_tuple[1][1][1][0])

# Задача 2.3
result = 0
week_set = ([80.0, 4500.5, 15505.0], [120.0, 450.0, 3300.0], [90.0, 2300.5, 10000.0], [160.0, 2100.5, 9500.0], [200.0, 4400.0, 8200.0], [80.0, 4000.5, 14000.0], [120.0, 6500.5, 24500.0])
for i in range(0, 7):
    for j in range(0, 3):
        result = result + week_set[i][j]
print(result)

# Задача 2.4
tuple_names = tuple(input().split())
print(*tuple(i for i in tuple_names if 'ва' in i or 'Ва' in i))

# Задача 2.5
text = input()
def transliterate(text):
    translate = "a b v g d e yo zh z i y k l m n o p \
                 r s t u f h ts ch sh shch y y ' e yu ya"

    dic = { chr(ru):translate for ru, translate in zip( \
        list(range(1072, 1078)) + [1105] + list(range(1078, 1104)), translate.split()) }

    dic.update({ chr(ru):translate for ru, translate in zip( \
        list(range(1040, 1046)) + [1025] + list(range(1046, 1072)), translate.title().split()) })

    new_text = ''
    for char in text:
        if char in dic:
            new_text += dic[char]
        else:
            new_text += char
    return new_text

print(transliterate(text))