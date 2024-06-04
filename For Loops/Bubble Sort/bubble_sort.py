def bubble_sort(lst, n):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


if __name__ == '__main__':
    num_list = input("Enter the list with a space in between each number: ").split()
    bubble_sort(num_list, len(num_list))
    print(num_list)
