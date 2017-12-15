
print("Your starting salary is just one penny but it doubles every day!!!")

numberOfDays = int(input("How many days will you work? "))
startSalary = 0.01
moneyEarned = 0
dayNumber = 0

for numberOfDays in range(numberOfDays,0,-1):
    dayNumber = dayNumber +1
    moneyEarned = moneyEarned + startSalary
    print("Salary for day",dayNumber,"today was:",startSalary)
    startSalary = startSalary * 2
    numberOfDays = numberOfDays - 1
print("You have earned",moneyEarned,"Dorrals in",dayNumber,"days" )

