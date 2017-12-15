sales = []
total = 0.0

def totalSales(sales, total):
    number = float(input("I'm waiting... \n"))
    if number < 0:
        for x in sales:
            total += x
        print("The sales are:", sales,"\n The final total is:",total)
    else:
        sales.append(number)
        totalSales(sales, total)


totalSales(sales, total)