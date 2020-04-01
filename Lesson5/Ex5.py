with open("text_gen_5.txt", "w", encoding="UTF-8") as text_file:
    text_file.write(input("ведите цифры через пробел: "))

with open("text_gen_5.txt", encoding="UTF-8") as text_file:
    numbers = text_file.read().split()
    num_sum = 0
    for num in numbers:
        num_sum += int(num)

print("Сумма всех чисел: ", num_sum)


