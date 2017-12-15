
print("Counting your loose change")

#Get the inputs
print("Enter the amount pennies you have \n")
pennies = int(input())
print("Enter the amount nickles you have \n")
nickels = int(input())
print("Enter the amount dimes you have \n")
dimes = int(input())
print("Enter the amount quarters you have \n")
quarters = int(input())

totalChange = pennies + nickels*5+dimes*10+quarters*25
if totalChange == 100:
    print("Congratulations you have exactly one dollar")
elif totalChange > 100:
    print("Oh you bee rich, you have",totalChange,"cents")
elif totalChange < 100:
    print("Oh your too poor, you can only find",totalChange,"cents in your pocket")
print(totalChange)