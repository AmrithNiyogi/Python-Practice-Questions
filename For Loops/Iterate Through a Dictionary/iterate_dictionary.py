def print_dictionary(d):
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")


if __name__ == '__main__':
    my_dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }
    print("Dictionary contents:")
    print_dictionary(my_dict)
