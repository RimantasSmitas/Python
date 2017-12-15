countyLoot = 0.0
stateLoot = 0.0

def main():

    totalPrice = int(input("Enter the price of purchase "))

    countyTax = 0.025
    stateTax = 0.05

    #stateTax = int(input("Enter the state tax "))
    #countyTax = int(input("Enter the county tax "))

    countyLoot = taxCalculator(totalPrice,countyTax)
    stateLoot = taxCalculator(totalPrice,stateTax)

    print("The price you payed to your county:", countyLoot, "American Dollars \n The tax you payed to your state:",
          stateLoot, "American Dollars")

def taxCalculator(price,Tax):

    loot = price * Tax
    loot = format(loot, ".2f")
    return loot

main()

