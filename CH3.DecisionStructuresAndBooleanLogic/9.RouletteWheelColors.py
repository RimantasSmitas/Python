
def blackBox ():
    colors = ["Green","Red","Black","Black","Red"]
    startMesage = "Choose a number on a roulette wheel and i'm gonna say what the color of that pocket is\n"
    print(startMesage)
    pocketNumber = int(input())
    pocketColor = ""
    section = [1,3]

    def pocketColorPrinter(pocketColor):
        print(pocketColor)
###\
    def ifingamachine(sectionnr):
        if pocketNumber % 2 == 0:
            sectionnr = int(sectionnr+1)
            pocketColor = colors[sectionnr]
            pocketColorPrinter(pocketColor)
        else:
            pocketColor = colors[sectionnr]
            pocketColorPrinter(pocketColor)

    if pocketNumber <0 or pocketNumber>36:
        print("There is no such number on a roulette wheel")
        blackBox()

    elif pocketNumber == 0:
        pocketColorPrinter("Green")
    else:
        if pocketNumber<11:
            ifingamachine(section[0])
        elif pocketNumber<19:
            ifingamachine(section[1])
        elif pocketNumber<28:
            ifingamachine(section[1])
        else:
            ifingamachine(section[0])

    yesno = str(input("do you want to know another one? "))
    if yesno == "y":
        blackBox()
    else:
        quit()
blackBox()