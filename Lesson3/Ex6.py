# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Выполнил с небольшим усложнением, заменяется только первая буква в каждом слове из строки


def int_func(text):
    new_text = ""
    words = text.split()
    for word in words:
        new_text = new_text + word[0].upper() + word[1:] + " "
    return new_text


user_text = input("Введите строку из слов: ")
print(int_func(user_text))
