# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('a1: '))
n = int(input('n: '))
d = int(input('d: '))
mAn = []
for i in range(1,n):
    an = a1 + (i-1) * d
    mAn.append(an)   
print(mAn)