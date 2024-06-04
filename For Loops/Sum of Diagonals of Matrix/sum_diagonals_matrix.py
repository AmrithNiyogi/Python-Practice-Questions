def sum_of_diagonal(m, s):
    diagonal_sum = 0
    for x in range(s):
        diagonal_sum += m[x][x]
    if s > 1:
        diagonal_sum += m[0][s - 1]
        diagonal_sum += m[s - 1][0]
    return diagonal_sum


if __name__ == '__main__':
    size = int(input("Enter the size of matrix: "))
    print("Enter the elements of the matrix: ")
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            element = int(input(f"Enter the element to be inserted at position ({i}, {j}): "))
            row.append(element)
        matrix.append(row)
    result = sum_of_diagonal(matrix, size)
    print(f"The sum of diagonals of the matrix {matrix} is: {result}")
