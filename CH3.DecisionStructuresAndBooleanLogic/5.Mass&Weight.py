
print("lets calculate the weight of the item in newtons")

mass = float(input("what's the items mass in kilograms? "))
g = 9.8

weight = mass * g

if weight > 500:
    print("It's too heavy")
elif weight < 100:
    print("It's too light")
else:
    print("It weghs just right")
print("It weighs",format(weight,".2f"),"newtons")
