
numberOfPurchasedShares = 2000
sharePurchasePrice = 40.00
numberOfSoldShares = 2000
shareSellingPrice = 42.75

totalShareCost = numberOfPurchasedShares*sharePurchasePrice
comisionForPurchase = totalShareCost*0.03
saleRevenue = numberOfSoldShares*shareSellingPrice
comisionForSale = saleRevenue*0.03
totalComision = comisionForPurchase+comisionForSale
moneyInTheEnd = saleRevenue - totalComision
profits = saleRevenue - totalShareCost - totalComision

print("Joe has bought some stocks of Acme.inc\n")
print("He payed:",format(totalShareCost,".2f"),"for the shares\n")
print("And",format(comisionForPurchase,".2f"),"to a broker named Pinky\n")
print("When he saw that share price has gone up")
print("He sold the stocks for a total of:",format(saleRevenue,".2f"))
print("But he had to pay:",format(comisionForSale,".2f"),"to a broker named Brain\n")
print("In the end he was left with",format(moneyInTheEnd,".2f"))
print("Which means his profits were",format(profits,".2f"))