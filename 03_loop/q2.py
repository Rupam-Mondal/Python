userNum = int(input("Enter a number = "))
sum_even = 0
for i in range(1 , userNum + 1):
    if userNum % 2 == 0:
        sum_even = sum_even + i
print(sum_even)