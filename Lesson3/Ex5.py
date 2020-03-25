# Вообще по моему использования глобальных переменных это плохо, но они были в уроке решил попробовать


def sum_number(numbers):
    global num_sum
    num_list = numbers.split()
    for num in num_list:
        if num == 'Q':
            break
        num_sum += int(num)


num_sum = 0
while True:
    user_numbers = input("Введите числа через пробел(для окончания программы нажмите Q): ").upper()
    sum_number(user_numbers)
    print("Общая сумма всех введеных чисел: ", num_sum)
    if user_numbers.find('Q') >= 0:
        break
