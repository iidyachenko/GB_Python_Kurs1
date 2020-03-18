# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.

number = int(input("Введите число: "))
max_num = number % 10
number = number // 10
while number != 0:
    ost = number % 10
    if ost > max_num:
        max_num = ost
    number = number // 10
print(max_num)
