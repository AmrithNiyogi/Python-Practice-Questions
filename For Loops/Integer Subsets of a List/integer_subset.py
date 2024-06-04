def find_subsets(nums):
    s_sets = []
    n = len(nums)
    num_subsets = 1 << n  

    for i in range(num_subsets):
        s_set = []
        for j in range(n):
            if i & (1 << j):  
                s_set.append(nums[j])
        s_sets.append(s_set)

    return s_sets


if __name__ == '__main__':
    numbers = list(map(int, input("Enter the list of integers separated by spaces: ").split()))
    subsets = find_subsets(numbers)

    print("The subsets are:")
    for subset in subsets:
        print(subset)
