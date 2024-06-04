def flatten_list(lst_of_lists):
    flat_list = []
    for sublist in lst_of_lists:
        for item in sublist:
            flat_list.append(item)
    return flat_list


if __name__ == "__main__":
    list_of_lists = eval(input("Enter a list of lists (e.g., [[1, 2], [3, 4, 5], [6]]): "))
    flattened_list = flatten_list(list_of_lists)
    print("Flattened list:", flattened_list)
