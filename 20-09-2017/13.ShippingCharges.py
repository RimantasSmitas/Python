print("I'm a shipping cost calculator\n")

weight = input("Enter the weight of package in pounds")

if weight > 10:
    costPerPound = 4.75
elif weight > 6:
    costPerPound = 4.00
elif weight > 2:
    costPerPound = 3.00
else:
    costPerPound = 1.50

totalCost = costPerPound*weight
print("It will cost you",totalCost,"USD to ship this item")
