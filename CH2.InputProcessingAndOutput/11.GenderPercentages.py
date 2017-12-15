numberOfWomen = int(input("How many Women are there in the class? "))
numberOfMen = int(input("How many Men are there in the class? "))

classTotal = numberOfMen+numberOfWomen
womenProcentage = numberOfWomen/classTotal*100
menProcentage = numberOfMen/classTotal*100

print("Women make up",format(womenProcentage,".2f"),"% of the class")
print("Men make up",format(menProcentage,".2f"),"% of the class")