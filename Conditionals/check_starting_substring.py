def starts_with(main_string, substring):
    if main_string.startswith(substring):
        print(f'The string "{main_string}" starts with "{substring}".')
    else:
        print(f'The string "{main_string}" does not start with "{substring}".')

        
if __name__ == '__main__':
    main_str = input("Enter the main string: ")
    sub_str = input("Enter the substring to check: ")

    starts_with(main_str, sub_str)
