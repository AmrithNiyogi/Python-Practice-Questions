def find_min(lst):
    min_num = lst[0]
    for item in lst:
        if min_num > item:
            min_num = item
    return min_num


def sum_list(lst):
    list_sum = 0
    for item in lst:
        list_sum += item
    return list_sum


if __name__ == '__main__':
    size = int(input("Enter size of list: "))
    print("Enter a list of numbers: ")
    numbers = []
    for num in range(size):
        num = int(input("Enter a number: "))
        numbers.append(num)

    print(f"List: {numbers}")

    minimum = find_min(numbers)
    print(f"The minimum value in the list {numbers} is: {minimum}")

    sum_num = sum_list(numbers)
    print(f"The sum of values in the list {numbers} is: {sum_num}")
  
