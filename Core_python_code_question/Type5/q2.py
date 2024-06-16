def reverse(nums):
    for i in range(0 , int(len(nums) / 2)):
        temp = nums[i]
        nums[i] = nums[len(nums) - i - 1]
        nums[len(nums) - i - 1] = temp

    return nums

nums = [1 , 2 , 3 , 4 , 5]
print(reverse(nums))