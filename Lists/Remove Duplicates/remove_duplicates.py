def remove_duplicates(s):
    new_list = []
    for item in s:
        if item not in new_list:
            new_list.append(item)
    return new_list


if __name__ == '__main__':
    numbers = [1, 2, 3, 1, 2, 4]
    print(f"List before removing duplicates: {numbers}")
    my_list = remove_duplicates(numbers)
    print(f"List after removing duplicates: {my_list}")
    
