class Date:
    data_str = ''

    def __init__(self, date):
        Date.data_str = date

    @staticmethod
    def data_check(day, month, year):
        if not day.isdigit() or 0 > int(day) > 31:
            print("Дата в неверном формате")
            return False

        if not month.isdigit() or 0 > int(month) > 12:
            print("Дата в неверном формате")
            return False

        if not year.isdigit() or 0 > int(year) > 9999:
            print("Дата в неверном формате")
            return False

        return True

    @classmethod
    def data_create(cls):
        if Date.data_check(cls.data_str[:2], cls.data_str[3:5], cls.data_str[6:10]):
            cls.day = int(cls.data_str[:2])
            cls.month = int(cls.data_str[3:5])
            cls.year = int(cls.data_str[6:10])
            print(f"День:{cls.day} Месяц:{cls.month} Год:{cls.year}")


date = Date('10.01.2010')
Date.data_create()
date = Date('10.янвварь.2010')
Date.data_create()
