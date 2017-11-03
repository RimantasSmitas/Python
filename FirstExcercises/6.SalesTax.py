totalPrice = int(input("Enter the price of purchase "))
countyTax = 0.025
stateTax = 0.05


stateLoot = totalPrice*stateTax
countyLoot = totalPrice*countyTax
stateLoot=format(stateLoot,".2f")
countyLoot=format(countyLoot,".2f")


print("The price you payed to your county:",countyLoot,"American Dollars \n The tax you payed to your state:",stateLoot,"American Dollars")
