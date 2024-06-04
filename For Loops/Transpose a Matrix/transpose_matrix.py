def transpose_matrix(mat):
    no_rows = len(mat)
    no_cols = len(mat[0])
    transposed = [[0] * no_rows for _ in range(no_cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = mat[i][j]

    return transposed


if __name__ == '__main__':
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))

    print("Enter the elements of the matrix row-wise:")
    matrix = []
    for k in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    transposed_mat = transpose_matrix(matrix)

    print("Transposed matrix:")
    for row in transposed_mat:
        print(row)
