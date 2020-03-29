numbers = input("Введите числа через пробел: ").split()
print(numbers)
result = [int(el) for el in numbers if numbers.count(el) == 1]
print(result)