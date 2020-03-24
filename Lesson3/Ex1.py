def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("На ноль делить нельязя!")


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(f"{a} делить на {b} = {division(a, b)}")
