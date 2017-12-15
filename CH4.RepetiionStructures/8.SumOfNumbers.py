print("I add positive numbers together if you try to be negative ill stop")
print("please enter as many number as you like")
sumOfNumbers = 0

def numberAdition(sumOfNumbers):
    number = int(input("I'm waiting... "))

    if number < 0:
        print("The final total is ",sumOfNumbers)
    else:
        sumOfNumbers +=  number
        numberAdition(sumOfNumbers)


numberAdition(sumOfNumbers)