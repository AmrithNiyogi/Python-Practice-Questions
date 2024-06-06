def convert_list_to_string(lst):
    return ', '.join(lst)


def convert_string_to_list(s):
    return s.split()


if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    result = convert_list_to_string(fruits)
    print(result)
    print()
    s = "apple banana cherry"
    result = convert_string_to_list(s)
    print(result)
