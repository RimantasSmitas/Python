print("Enter a number and i'll calculate a factorial for it")

runningTotal = 1
startNumber = int(input())
number = startNumber


for number in range (number,0,-1):
    runningTotal *= number

print("The factorial of",startNumber,"is",runningTotal)