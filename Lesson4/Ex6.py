from itertools import count, cycle


# Попробовал реализовать ва скрипта в одном. выводим номер итерации и значние из масива.
count_step = int(input("Введите число повторений: "))
my_list = input("Введите слова через пробел: ").split()
word = cycle(my_list)
for el in count(1):
    if el > count_step:
        break
    else:
        print(el, next(word))




