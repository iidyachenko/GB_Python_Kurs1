class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


input_list = []
while True:
    inp_data = input("Введите число(для окончания ввода нажмите stop): ")
    if inp_data == 'stop':
        break
    try:
        if not inp_data.isdigit():
            raise OwnError("Вы ввели не число!")
        inp_data = int(inp_data)
        input_list.append(inp_data)
    except OwnError as err:
        print(err)

print(input_list)