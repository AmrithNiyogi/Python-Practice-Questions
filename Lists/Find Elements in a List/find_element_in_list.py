def index_of(element, lst):
    index = 0
    for num in lst:
        if num == element:
            return index
        index += 1
    return -1


def contains(element, lst):
    if element in lst:
        return True
    return False


if __name__ == '__main__':
    my_list = []
    size = int(input("Enter size of list: "))
    print("Enter values into the list: ")
    for _ in range(size):
        item = int(input("Enter item: "))
        my_list.append(item)

    search_element = int(input("Enter element to search: "))

    if contains(search_element, my_list):
        print(f"{search_element} is present in the list {my_list}")
        position = index_of(search_element, my_list)
        print(f"{search_element} is at index: {position}")
    else:
        print(f"{search_element} not in the list")
