# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("text2.txt", encoding='UTF-8') as text_file:
    text_list = text_file.readlines()

text_list = [line.rstrip() for line in text_list]  # Убираем разделители строки и пробелы в конце строки
print("Всего строк: ", len(text_list))
for words in text_list:
    print(words, " Слов в строке: ", len(words.split()))
