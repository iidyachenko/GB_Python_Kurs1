# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

eng_list = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text4.txt", encoding='UTF-8') as text_file:
    out_file = open("text_gen_4.txt", "w", encoding="UTF-8")
    for line in text_file:
        word = eng_list[line[:line.find("-")-1]] + line[line.find("-")-1:]
        out_file.write(word)
    out_file.close()
