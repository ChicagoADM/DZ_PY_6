# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import os
clear = lambda: os.system('cls')
clear()
from functools import reduce
dot_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split()))
print() 
dot_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
print()
def dot_range(dot_1, dot_2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(rng, 2)
print(f'Расстояние между двух точек 2D пространстве = {dot_range(dot_1, dot_2)}')
print()
input('Нажмите Enter для выхода ...')