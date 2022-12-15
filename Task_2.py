# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
import os
clear = lambda: os.system('cls')
clear()
from math import factorial
n = int(input('Введите число: '))
print()
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,n+1)))))
print()
input('Нажмите Enter для выхода ...')