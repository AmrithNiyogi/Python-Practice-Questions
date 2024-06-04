def print_histogram(d):
    for value in d:
        print('*' * value)


if __name__ == '__main__':
    data = list(map(int, input("Enter the list of integers separated by spaces: ").split()))
    print("Histogram:")
    print_histogram(data)
