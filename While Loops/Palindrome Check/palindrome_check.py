def is_palindrome(s):

    left_index = 0
    right_index = len(s) - 1

    while left_index < right_index:
        if s[left_index] != s[right_index]:
            return False
        left_index += 1
        right_index -= 1

    return True


if __name__ == "__main__":
    input_string = input("Enter a string to check if it is a palindrome: ")
    if is_palindrome(input_string):
        print(f"'{input_string}' is a palindrome.")
    else:
        print(f"'{input_string}' is not a palindrome.")
