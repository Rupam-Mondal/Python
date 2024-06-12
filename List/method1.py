tea = ["Black" , "Green" , "Oolong"]

print(tea)

print(tea[-1])
print(tea[1:2])
tea[0] = "Coffee"
print(tea)

tea[1:2] = "Lemon"
print(tea)

tea[1:2] = ["Lemon"]
print(tea)

for a in tea:
    print(a)

if "Oolong" in tea:
    print("I have Oolong")