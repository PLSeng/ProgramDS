from BMatrix import BMatrix
from Cal_Matrix import Cal_Matrix

class Matrix_Full(BMatrix):

    def __init__(self, data: list[list[float]]):
        super().__init__(data)

    def transpose(self) -> 'Matrix_Full':
        result = [[self.element_at(l, c) for l in range(self.nl)] for c in range(self.nc)]
        return Matrix_Full(result)

    def identity(self) -> 'Matrix_Full':
        if self.nl == self.nc:
            result = [[1 if l == c else 0 for c in range(self.nc)] for l in range(self.nl)]
            return Matrix_Full(result)
        else:
            raise ValueError("Matrix must be square")

    def __add__(self, other: 'Matrix_Full') -> 'Matrix_Full':
        return Cal_Matrix.add(self, other)

    def __sub__(self, other: 'Matrix_Full') -> 'Matrix_Full':
        return Cal_Matrix.subtract(self, other)

    def __mul__(self, other: 'Matrix_Full') -> 'Matrix_Full':
        return Cal_Matrix.multiply(self, other)

    def scalar(self, scalar: float) -> 'Matrix_Full':
        return Cal_Matrix.multiply_by_scalar(self, scalar)

    def show(self):
        print(self)
