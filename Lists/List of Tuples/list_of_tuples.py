def sum_of_first_elements(tuples):
    sum_elements = 0
    for t in tuples:
        sum_elements += t[0]
    return sum_elements


if __name__ == '__main__':
    squares_list = []
    for x in range(1, 6):
        element = x ** 2
        squares_list.append((x, element))
    print(squares_list)
    result = sum_of_first_elements(squares_list)
    print(f"The sum of the first elements of each tuple in the list {squares_list} is:\n {result}")
