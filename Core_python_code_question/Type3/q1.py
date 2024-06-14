usernumber = int(input("Enter a Number = "))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


ans = factorial(usernumber)
print(f"Answer is = {ans}")