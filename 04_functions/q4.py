import math

def calculation(n):
    area = math.pi * n ** 2
    cir = 2 * math.pi * n
    return area , cir

a , c = calculation(3)
print("Area : " , a , "Cir : " , c)