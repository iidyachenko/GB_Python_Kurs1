# Расчет экономической деятельности фирмы

revenue = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
profit = revenue - cost
if profit > 0:
    rent = (profit/revenue)*100
    print("Ваша прибыль составила: ", profit)
    print(f"Ваша рентабльность: {rent:.2f}%")
    staff = int(input("Введите численость персонала: "))
    staff_profit = profit / staff
    print(f"Ваша прибыль на одного сотрудника составила: {staff_profit:.2f}")
else:
    print("Выши расходы превышают доходы, ваш баланс: ", profit)
