class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in j.split()]
            for j in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix[index - 1].copy()

    def column(self, index):
        return [x[index - 1] for x in self.matrix]