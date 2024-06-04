def maximum(lst):
    max_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i

    return max_num


if __name__ == '__main__':
    num_list = input("Enter the first list of numbers separated by spaces: ").split()
    converted_list = []
    for x in num_list:
        converted_list.append(int(x))
    num_list = converted_list
    maximum_number = maximum(num_list)
    print(f"The maximum value in the list {num_list} is: {maximum_number}")
    
