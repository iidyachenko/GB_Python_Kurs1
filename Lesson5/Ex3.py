# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("text3.txt", encoding='UTF-8') as text_file:
    text_list = [text.split() for text in text_file.read().split("\n")]

salary = 0.0
print("Сотрудники с ЗП меньше 20 тысяч: ")
for employee in text_list:
    salary += float(employee[1])
    if float(employee[1]) < 20000:
        print(employee[0], employee[1])

print(f"Средний доход всех сотрудников: {salary/len(text_list):.2f}")