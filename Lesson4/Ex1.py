from sys import argv


def salary(work_hour, hour_pay, bonus):
    result = int(work_hour) * int(hour_pay) + int(bonus)
    return result


script_name, work_hours, pay_hours, bonus_money = argv
print("Заработная плата = ", salary(work_hours, pay_hours, bonus_money))