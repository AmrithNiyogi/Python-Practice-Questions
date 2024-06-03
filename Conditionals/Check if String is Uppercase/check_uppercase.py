def check_uppercase(s):
    s1 = s.upper()
    if s1 == s:
        print("All letters are Uppercase")
    else:
        print("Not all letters are Uppercase")


if __name__ == '__main__':
    string = input("Enter a word to check if it is uppercase: ")
    check_uppercase(string)
