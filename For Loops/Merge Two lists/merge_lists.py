def merge_and_sort_lists(l1, l2):
    merged_list = []
    for item in l1:
        if item not in merged_list:
            merged_list.append(item)

    for item in l2:
        if item not in merged_list:
            merged_list.append(item)

    for i in range(len(merged_list)):
        for j in range(i + 1, len(merged_list)):
            if merged_list[i] > merged_list[j]:
                merged_list[i], merged_list[j] = merged_list[j], merged_list[i]

    return merged_list


if __name__ == '__main__':
    list1 = input("Enter the first list of numbers separated by spaces: ").split()
    converted_list1 = []
    for x in list1:
        converted_list1.append(int(x))
    list1 = converted_list1

    list2 = input("Enter the second list of numbers separated by spaces: ").split()
    converted_list2 = []
    for x in list2:
        converted_list2.append(int(x))
    list2 = converted_list2

    result = merge_and_sort_lists(list1, list2)

    print("Merged and sorted list without duplicates:", result)
