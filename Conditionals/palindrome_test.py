def palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


if __name__ == '__main__':
    string = input("Enter a word to check if it is a palindrome: ")
    palindrome(string)
