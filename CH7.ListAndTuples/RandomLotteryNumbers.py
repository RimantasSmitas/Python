import random
list = []

def randomDigit(list):
    randInt = random.randrange(10)
    list.append(randInt)

for x in range(7):
    randomDigit(list)
print ("Your lucky numbres are",list)