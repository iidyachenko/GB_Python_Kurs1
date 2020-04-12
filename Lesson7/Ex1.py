class Matrix:
    matr_str = ''

    def __init__(self, my_list):
        self.matr_list = my_list

    def __str__(self):
        for i in self.matr_list:
            for j in i:
                self.matr_str += ' ' + str(j)
            self.matr_str += '\n'
        return self.matr_str

    def __add__(self, matrix):
        new_list = []
        for i in range(0, len(self.matr_list)):
            new_list_j = []
            for j in range(0, len(self.matr_list[i])):
                new_list_j.append(int(self.matr_list[i][j]) + int(matrix.matr_list[i][j]))
            new_list.append(new_list_j)
        return Matrix(new_list)


matr1 = Matrix([["1", "2", "3"], ["4", "5", "6"]])
matr2 = Matrix([["10", "20", "30"], ["40", "50", "60"]])
matr3 = matr1 + matr2
print(matr1)
print(matr2)
print(matr3)
