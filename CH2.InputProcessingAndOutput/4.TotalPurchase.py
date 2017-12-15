itemCount = int(input("how many are you buying "))
totalPrice = 0.0
price = 0.0

while (itemCount > 0):
    price = input("type in the price of item\n")
    totalPrice = (float(price) + totalPrice)
    print("Your subtotal is:",totalPrice)
    itemCount = (itemCount - 1)

salesTax = totalPrice*0.07
print("Your total is",totalPrice,"\n sales tax is:",salesTax)
