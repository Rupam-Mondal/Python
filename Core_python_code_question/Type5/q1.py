def duplicate(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

nums = [2 , 3 , 4 , 4 , 6 , 7 , 8 , 8]

print(duplicate(nums))