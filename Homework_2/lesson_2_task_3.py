import math

def square( side_square):
    return math.ceil(side_square * side_square)

side = float(input('Введите длину стороны квадрата: '))
area = square(side)
print(f'Площадь квадрата: {area}')