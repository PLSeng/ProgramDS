from BMatrix import BMatrix

class Cal_Matrix():

    @staticmethod
    def add(matrix1: 'BMatrix', matrix2: 'BMatrix'):
        if matrix1.same_size(matrix2):
            result = [[matrix1.element_at(l, c) + matrix2.element_at(l, c) for c in range(matrix1.nc)] for l in
                      range(matrix1.nl)]
            return BMatrix(result)
        else:
            raise ValueError("Matrices must have the same size")

    @staticmethod
    def subtract(matrix1: 'BMatrix', matrix2: 'BMatrix'):
        if matrix1.same_size(matrix2):
            result = [[matrix1.element_at(l, c) - matrix2.element_at(l, c) for c in range(matrix1.nc)] for l in
                      range(matrix1.nl)]
            return BMatrix(result)
        else:
            raise ValueError("Matrices must have the same size")

    @staticmethod
    def multiply(matrix1: 'BMatrix', matrix2: 'BMatrix'):
        if matrix1.nc == matrix2.nl:
            result = [[sum(matrix1.element_at(l, i) * matrix2.element_at(i, c) for i in range(matrix1.nc)) for c in
                       range(matrix2.nc)] for l in range(matrix1.nl)]
            return BMatrix(result)
        else:
            raise ValueError(
                "Number of columns of the first matrix must be equal to the number of rows of the second matrix")

    @staticmethod
    def multiply_by_scalar(matrix: 'BMatrix', scalar: float):
        result = [[matrix.element_at(l, c) * scalar for c in range(matrix.nc)] for l in range(matrix.nl)]
        return BMatrix(result)
