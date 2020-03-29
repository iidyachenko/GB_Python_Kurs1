from functools import reduce

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.


def my_func(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1000) if el % 2 == 0]
print(my_list)
print(reduce(my_func, my_list))
