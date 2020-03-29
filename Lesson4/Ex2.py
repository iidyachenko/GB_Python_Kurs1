numbers = input("Введите числа через пробел: ").split()
print(numbers)
result_numbers = [int(numbers[i]) for i in range(0, len(numbers)) if int(numbers[i]) > int(numbers[i-1])]
print(result_numbers)
