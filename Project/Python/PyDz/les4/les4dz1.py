# Задача 1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random
A=[]
B=[]
n,m = map(int, input('Введите n и m количество элементов множеств: ').split())
for i in range(n):
    A.append(random.randint(1, 20))
print (f'Исходный массив A: {A}')

for i in range(m):
    B.append(random.randint(1, 20))
print (f'Исходный массив B: {B}')

i = sorted(set(A).intersection(set(B)))
print (f'Повторяющиеся числа: {i}')