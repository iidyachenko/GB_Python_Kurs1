# создадим калькулятор
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

sum = a + b
print(f"Сумма чисел {a} и {b} = {sum}")
dif = a - b
print(f"Разность чисел {a} и {b} = {dif}")
mult = a * b
print(f"Произведение чисел {a} и {b} = {mult}")
div = a / b
print(f"Частное чисел {a} и {b} = {div:.2f}")
