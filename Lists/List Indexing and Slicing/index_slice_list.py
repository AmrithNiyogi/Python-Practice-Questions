if __name__ == '__main__':
    # creating the list
    num_list = [10, 20, 30, 40, 50]
    # print the third number
    # 3rd number is the 2nd index
    third_num = num_list[2]
    print(f"The third element of the list {num_list} is: {third_num}")
    # printing the last two numbers
    last_two_numbers = num_list[3:]
    print(f"The last two element of the list {num_list} is: {last_two_numbers}")
    # printing every second element in the list
    even_index_list = num_list[0::2]
    print(f"Every second element of the list {num_list} are: {even_index_list}")
