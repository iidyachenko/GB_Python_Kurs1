# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
              "Июль", 'Август', "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

month_dict = {"Январь": "Зима", "Февраль": "Зима", "Март": "Весна", "Апрель": "Весна", "Май": "Весна", "Июнь": "Лето",
              "Июль": "Лето", 'Август': "Лето", "Сентябрь": "Осень", "Октябрь": "Осень", "Ноябрь": "Осень",
              "Декабрь": "Зима"}

month_num = int(input("Введите номер месяца от 1 до 12: "))
print(f"Вы выбрали {month_list[month_num - 1]}. Время года {month_dict[month_list[month_num - 1]]}")
