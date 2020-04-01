import json


profit_dict = {}
with open("text_7.txt", encoding='UTF-8') as text_file:
    total_profit = 0
    profit_firm = 0
    for line in text_file:
        key = line.split()[0]
        value = int(line.split()[2]) - int(line.split()[3])
        profit_dict[key] = value
        if value > 0:
            total_profit += value
            profit_firm += 1

avg_profit_dict = {"average_profit": total_profit/profit_firm}
result_list = [profit_dict, avg_profit_dict]
print(result_list)

with open("jfile7.json", "w", encoding="UTF-8") as out_file:
    json.dump(result_list, out_file, ensure_ascii=False, indent=4)