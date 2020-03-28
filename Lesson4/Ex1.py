from sys import argv


def salary(work_hour, hour_pay, bonus):
    result = work_hour * hour_pay + bonus
    return result


script_name, work_hours, pay_hours, bonus_money = argv
print("Заработная плата = ", salary(work_hours, pay_hours, bonus_money))