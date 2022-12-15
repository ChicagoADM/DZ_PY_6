# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
import os
clear = lambda: os.system('cls')
clear()
n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print()
print (f'Cумму цифр вещественное число: {sum}')
print()
input('Нажмите Enter для выхода ...')