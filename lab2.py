# Лабораторная работа №2
'''
Arslan!
'''
name = input('Введите имя: ')
print('Привет, ' + name + '!')

age = int(input('Введите возраст: '))
if(age > 0 and age < 18) :
    print('Вы не совершеннолетний!')
elif(age > 18) :
    print('Вы дед!')
else :
    print('Вы не пойми кто!')