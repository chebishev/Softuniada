matrix_size = int(input())

matrix = []

for row in range(matrix_size):
    matrix.append(input().split())

new_matrix = []
for i in range(matrix_size):
    new_matrix.append([])
    for j in range(matrix_size):
        new_matrix[i].append(matrix[matrix_size - 1 - j][i])
    print(*new_matrix[i], sep=" ")
