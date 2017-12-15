itemCount = int(input("How many dishes have you had? "))
totalPrice = 0.0
price = 0.0

while (itemCount > 0):
    price = float(input("type in the price of dish "))
    totalPrice = price + totalPrice
    print("Your subtotal is:",format(totalPrice,".2f"))
    itemCount = (itemCount - 1)

salesTax = format((totalPrice*0.07),".2f")
tip = format((totalPrice*0.18),".2f")
print("Your total is",totalPrice,"\n sales tax is:",salesTax,"\n The appropriate tip is: ",tip)
