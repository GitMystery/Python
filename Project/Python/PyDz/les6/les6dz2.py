# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
n = int(input('n: '))
min1 = int(input('min: '))
max1 = int(input('max: '))
a=[]
for i in range(n):
    a.append(random.randint(min1, max1))
print (f'Исходный массив A: {a}')
k = int(input('Введите искомое число для нахождения индекса: '))
for i in range(n):
    if a[i]==k:
        print (f'Число {k} имеет индекс: {i}')
