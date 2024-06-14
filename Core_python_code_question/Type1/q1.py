def swap(a , b):
    a = a + b
    b = a - b
    a = a - b

    return a , b

a = 5
b = 3

c , d = swap(a , b)

print(f"Value of a is = {c} , value of b is = {d}")