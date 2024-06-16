nums = (3 , 4 , 6 , 11 ,10 , 12)

def delSecondLargest(nums):
    arr =list(nums)
    max = arr[0]
    for i in range(0 , len(nums)):
        if max < arr[i]:
            max = arr[i]

    for i in range(0 , len(nums)):
        if arr[i] == max:
            arr[i] = 0
    max = arr[0]
    for i in range(0 , len(nums)):
        if max < arr[i]:
            max = arr[i]

    return max

print(delSecondLargest(nums))