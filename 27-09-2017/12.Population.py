print("We're gonna count some microbes")

startNumber = int(input("Enter the number of germs "))
dailyIncrease = int(input("Enter the average daily increase in procentage "))
numberOfDays = int(input("Enter the number of days the experiment is going to last "))
daycount = 0

print("Day Approximate \t \t Population")

for numberOfDays in range(numberOfDays,0,-1):
    daycount = daycount +1
    print(daycount, "\t\t", startNumber)
    startNumber = startNumber*(1+dailyIncrease/100)

