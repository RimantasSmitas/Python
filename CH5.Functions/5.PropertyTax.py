print("i calculate assesment tax the county collects")

def Getter():
    value = float(input(("Please enter the value of your property ")))
    Calculator(value)

def Calculator(value):
     assesmentValue = value * 0.6
     propertyTax = assesmentValue * 0.0072
     GoodNewsEveryone(assesmentValue,propertyTax)

def GoodNewsEveryone(assesmentValue,propertyTax):
    print("Your assesment value is ",format(assesmentValue,".2f"))
    print("You will be taxed a ludicrous",format(propertyTax,".2f"),"dolars")


Getter()
iffer = input("Do you want to do more calculations y/n?")
if iffer == "y":
    Getter()

