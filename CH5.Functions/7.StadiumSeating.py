aSeat = 20
bSeat = 15
cSeat = 10


def main():
    aCount = int(input("How many a seats were sold?"))
    bCount = int(input("How many b seats were sold?"))
    cCount = int(input("How many c seats were sold?"))
    Calculator(aCount,bCount,cCount)

def Calculator(aCount,bCount,cCount):
    totalprice = (aCount * aSeat) + (bCount*bSeat)+(cCount+cSeat)
    Printer(totalprice)


def Printer(message):
    print("total income was: ",message)

main()