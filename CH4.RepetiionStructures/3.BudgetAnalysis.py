print("I'm a burocratic budgeting robot")

alocatedFunds = float(input("Enter the amount you have budgeted for this month "))
currentExpense = 1
runningTotal = 0
diference = alocatedFunds
print("Enter youre expenses,\nIf you type in zero the program will show you a running expenses total\n And the diference between the estimate and actual")

while currentExpense != 0:
    currentExpense =  float(input())
    runningTotal =  currentExpense + runningTotal
    diference = float(diference - currentExpense)
    print("Your running total is:", runningTotal)
print("The difrence between your estimate and total is",diference)
