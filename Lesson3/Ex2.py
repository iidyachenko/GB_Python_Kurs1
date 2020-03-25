# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def person_data(name, surname, year, city, email, phone):
    print(f"Меня зовут {name} {surname}, я {year} года рождения, живу в городе {city}. "
          f"Мой email: {email}, мой телефон: {phone}")


my_name = input("Введите ваше имя: ")
my_surname = input("Введите вашу фамилию: ")
my_year = input("Введите год рождения: ")
my_city = input("Введите город проживания: ")
my_email = input("Введите электронную почту: ")
my_phone = input("Введите номер телефона: ")

person_data(name=my_name, surname=my_surname, year=my_year, city=my_city, email=my_email, phone=my_phone)

