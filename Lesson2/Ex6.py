i = 0
product_list = []
while True:
    name = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    quantity = input("Введите количество товара: ")
    unit = input("Введите единицу измерения: ")
    product_dict = {"название": name, "цена": price, "количество": quantity, "eд": unit}
    i += 1
    product_tuple = (i, product_dict)
    product_list.append(product_tuple)
    user_choice = input("Для ввода еще одного товара введите 'Y': ")
    if user_choice != "Y" and user_choice != 'y':
        break

print(product_list)

# можно было использовать множества тогда не нужно было бы делать проверки на вхождение,
# но в задании судя по скобкам нужно использовать список.
name_list = []
price_list = []
quantity_list = []
unit_list = []

for product in product_list:
    if product[1]["название"] not in name_list:
        name_list.append(product[1]["название"])
    if product[1]["цена"] not in price_list:
        price_list.append(product[1]["цена"])
    if product[1]["количество"] not in quantity_list:
        quantity_list.append(product[1]["количество"])
    if product[1]["eд"] not in unit_list:
        unit_list.append(product[1]["eд"])

product_dict = {"название": name_list, "цена": price_list, "количество": quantity_list, "eд": unit_list}
print(product_dict)
