def check_letter(ch):
    if ch in 'aeiou':
        print(f"{ch} is a Vowel")
    else:
        print(f"{ch} is a Consonant")


if __name__ == '__main__':
    letter = input("Enter a letter: ")
    check_letter(letter)
    