def check_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if sorted(s1) == sorted(s2):
        print("Anagrams")
    else:
        print("Not anagrams")


if __name__ == '__main__':
    string1 = input("Enter word 1: ")
    string2 = input("Enter word 2: ")
    check_anagram(string1, string2)
