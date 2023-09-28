# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
#
def transpose_matrix(matrix: list[list]) -> list[list]:
    new_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


matrix = [[1, 2, 3], [4, 5, 6]]
print(f'Изначальная матрица:\n {matrix}\nТранспонирование матрицы:\n {transpose_matrix(matrix)}')
