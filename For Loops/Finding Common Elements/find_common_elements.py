def find_common_elements(l1, l2):
    common_elem = []
    for item in l1:
        if item in l2 and item not in common_elem:
            common_elem.append(item)
    return common_elem


if __name__ == "__main__":
    list1 = input("Enter elements of the first list separated by spaces: ").split()
    list2 = input("Enter elements of the second list separated by spaces: ").split()

    common_elements = find_common_elements(list1, list2)

    if common_elements:
        print("Common elements between the two lists are:", common_elements)
    else:
        print("There are no common elements between the two lists.")
