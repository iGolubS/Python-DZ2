# 4. Напишите программу, которая на вход принимает 2 числа. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов на указанных позициях (не индексах).

numN = int(input('Введите число N: '))
list = []
for i in range(-numN,numN+1):
    list.append(i)
print(list)
position1 = int(input('Укажите первую позицию цифры из списка, которую нужно перемножить: '))
position2 = int(input('Укажите вторую позицию цифры из списка, которую нужно перемножить: '))
print(f'Произведение чисел = {list[(position1-1)]*list[(position2-1)]}')