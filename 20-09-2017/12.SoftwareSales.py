print("We're gonna count the discount you're entitled to")

unitCount = int(input("How many units did you buy? "))

if unitCount >= 100:
    discountP = 0.4
elif unitCount >= 50:
    discountP = 0.3
elif unitCount >= 20:
    discountP = 0.2
elif unitCount >= 10:
    discountP = 0.1

price = unitCount * 99
discountSize = discountP*price
priceAfterDiscount = price - discountSize

print("Price before discount:",price)
print("Your discount size is:",discountSize)
print("Your price after discount is:",priceAfterDiscount)


