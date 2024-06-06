if __name__ == '__main__':
    # Create a list of tuples containing each letter in "hello" and its corresponding ASCII value
    word = input("Enter a word: ")
    ascii_list = [(char, ord(char)) for char in word]
    print(ascii_list)
    # Create a flattened list from a list of lists
    nested_list = [[1, 2, 3], [4, 5], [6]]
    flattened_list = [item for sublist in nested_list for item in sublist]
    print(flattened_list)
