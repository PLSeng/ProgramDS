from Matrix_Full import Matrix_Full


class Main2:
    matrix1 = Matrix_Full([[1, 2], [3, 4]])
    matrix2 = Matrix_Full([[5, 6], [7, 8]])
    matrix3 = matrix1 + matrix2
    matrix4 = matrix1 - matrix2
    matrix5 = matrix1 * matrix2
    matrix6 = matrix1.scalar(2)
    matrix7 = matrix1.transpose()
    matrix8 = matrix1.identity()
    print("Matrix 1:")
    matrix1.show()
    print("Matrix 2:")
    matrix2.show()
    print("Matrix 3 = Matrix 1 + Matrix 2:")
    matrix3.show()
    print("Matrix 4 = Matrix 1 - Matrix 2:")
    matrix4.show()
    print("Matrix 5 = Matrix 1 * Matrix 2:")
    matrix5.show()
    print("Matrix 6 = Matrix 1 * 2:")
    matrix6.show()
    print("Matrix 7 = Transpose of Matrix 1:")
    matrix7.show()
    print("Matrix 8 = Identity matrix of Matrix 1:")
    matrix8.show()
    print('Does Matrix 1 have the same size as Matrix 2?: ', matrix1.same_size(matrix2))
    print('Element at row 1, column 1 of Matrix 1:', matrix1.element_at(1, 1))
    print()
