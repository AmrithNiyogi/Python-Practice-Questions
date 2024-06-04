def compress_string(s):
    if not s:
        return ""

    compressed_string = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_string += s[i - 1] + str(count)
            count = 1

    compressed_string += s[-1] + str(count)
    return compressed_string

if __name__ == "__main__":
    input_string = input("Enter a string to compress: ")
    compressed_string = compress_string(input_string)
    print("Compressed string:", compressed_string)
