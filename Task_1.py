# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import os
clear = lambda: os.system('cls')
clear()
import math
list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print()
print('Исходный список: ',list_a)
print()
print('Результат: ',list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))
print()
input('Нажмите Enter для выхода ...')