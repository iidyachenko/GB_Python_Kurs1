lesson_dict = {}
with open("text_6.txt", encoding='UTF-8') as text_file:
    for line in text_file:
        key = line[:line.find(":")]
        value_list = line[line.find(":") + 1:].split()
        value = [int(el[:el.find("(")]) for el in value_list if el != '-']
        lesson_dict[key] = sum(value)
print(lesson_dict)
