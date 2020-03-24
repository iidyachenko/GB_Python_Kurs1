def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return my_list[1] + my_list[2]


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите первое число: "))
num3 = int(input("Введите первое число: "))
s = my_func(num1, num2, num3)
print(f"Сумма двух наибольших чисел = {s}")
