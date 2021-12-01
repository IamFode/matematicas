#diagonal de una función
array = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

def matrix_diag(matrix):
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
    return diagonal

print(matrix_diag(array))
