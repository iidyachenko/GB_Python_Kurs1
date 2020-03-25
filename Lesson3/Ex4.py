def my_minus_pow1(num, minus_pow):
    """Первый вариант решения"""
    return 1 / (num ** abs(minus_pow))


def my_minus_pow2(num, minus_pow):
    """Второй вариант решения"""
    pow_sum = num
    for i in range(1, abs(minus_pow)):
        pow_sum = pow_sum * num
    return 1 / pow_sum


x = float(input("Введите действительное положительное число: "))
y = int(input("Введите целое отрицательное число: "))
result = my_minus_pow1(x, y)
print(result)
result = my_minus_pow2(x, y)
print(result)
