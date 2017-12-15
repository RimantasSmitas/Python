print("Lets find out if the date is magic")

day = int(input("Please enter day number "))
month = int(input("Please the number of the month "))
year = int(input("Please enter the last two digits of the year "))

if (month*day == year):
    print("Its a magic day!!!")
else:
    print("The day isn't magic :(")
