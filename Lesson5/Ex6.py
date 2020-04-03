# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

lesson_dict = {}
with open("text_6.txt", encoding='UTF-8') as text_file:
    for line in text_file:
        key = line[:line.find(":")]
        value_list = line[line.find(":") + 1:].split()
        value = [int(el[:el.find("(")]) for el in value_list if el != '-']
        lesson_dict[key] = sum(value)
print(lesson_dict)
