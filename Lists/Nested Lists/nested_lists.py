def print_matrix(mat):
    for r in mat:
        print(r)


if __name__ == '__main__':
    matrix = []
    for _ in range(2):
        row = []
        for _ in range(3):
            row.append(1)
        matrix.append(row)
    print_matrix(matrix)
