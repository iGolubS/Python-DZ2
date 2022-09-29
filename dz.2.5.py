# 5. Реализуйте алгоритм перемешивания списка. Без функции shuffle.

import random
list = [random.randint(0,10) for i in range(random.randint(5,20))]
print(f"Исходный список:\n{list}")
def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list
mixed_list = mix_list(list)
print("Перемешанный список: ")
print(mixed_list)