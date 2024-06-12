userage = int(input("Enter your age = \n"))
if userage < 20 and userage >= 0:
    print("Age group between 0 to 19\n")
elif userage >= 20 and userage <= 60:
    print("Age group 20 to 60")
else:
    print("You are old")