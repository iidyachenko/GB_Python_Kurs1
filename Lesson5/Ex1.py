# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

text = ''
while True:
    string = input("Введите строку: ")
    if string == '':
        break
    else:
        text += string + '\n'
        print(string)

# решил записать все строи разом, что бы не открывать файл в цикле каждый раз.
with open("text_gen_1.txt", 'w', encoding='UTF-8') as text_file:
    text_file.write(text)
print(text)