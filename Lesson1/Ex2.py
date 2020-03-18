input_sec = int(input("Введите количество секунд: "))
hours = input_sec // 3600
ost = input_sec % 3600
min = ost // 60
sec = ost % 60
print(f"{hours:02}:{min:02}:{sec:02}")
