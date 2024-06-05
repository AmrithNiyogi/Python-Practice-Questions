def add_matrix(m1, m2):
    result_mat = []
    for x in range(len(m1)):
        r = []
        for y in range(len(m1[0])):
            r.append(m1[x][y] + m2[x][y])
        result_mat.append(r)

    return result_mat


if __name__ == '__main__':
    size = int(input("Enter the size of matrix: "))
    print("Enter the elements of the matrix 1: ")
    matrix1 = []
    for i in range(size):
        row = []
        for j in range(size):
            element = int(input(f"Enter the element to be inserted at position ({i}, {j}) of matrix 1: "))
            row.append(element)
        matrix1.append(row)

    print("Enter the elements of the matrix 2: ")
    matrix2 = []
    for i in range(size):
        row = []
        for j in range(size):
            element = int(input(f"Enter the element to be inserted at position ({i}, {j}) of matrix 2: "))
            row.append(element)
        matrix2.append(row)

    result = add_matrix(matrix1, matrix2)
    print(f"The sum of {matrix1} + {matrix2} is: {result}")
