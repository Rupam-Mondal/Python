userage = int(input("Enter your age = \n"))
if userage < 20 and userage >= 0:
    print("Ticket price is 12 dollar\n")
elif userage >= 20 and userage <= 60:
    print("Ticket price is 50 dollar")
else:
    print("Ticket price is 100 dollar")