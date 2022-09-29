# 3. Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

numN = int(input('Введите число N: '))
temp = 1
dic = {}
sum = 0
for temp in range(1,numN+1):
    dic[temp] = round((1+1/temp)**temp, 3)
    sum = sum + dic[temp]
    temp += 1
print(dic)
print(sum)