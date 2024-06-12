ele1 = "    Rupam"
print(ele1.strip())

print(ele1.replace("Ru" , "Ku"))

ele1.split() #This splicts a list according to user demand may be 
#with respect to  , space . etc

ele1.find(" ") #finds char or part of string index in string
ele1.count(" ") # counts number of portion or character

elements = ["ion" , "Iron" , "Gold"]
print(",".join(elements))

print(len(ele1))

for c in ele1:
    print(c)

ex2 = "He said , \"Paris is awesome\" "
print(ex2)

ex3 = r"op\nop1" #adding r will print raw string
print(ex3)