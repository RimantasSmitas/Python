print("I'm a bug calculator\n")

dayCount = int(input("How many days are you gonna pick the bugs? "))
bugCount = 0

while dayCount > 0:
    bugsOfTheDay = int(input("How many bugs have you collected? "))
    bugCount = bugCount + bugsOfTheDay
    dayCount = dayCount - 1

print("You have collected",bugCount,"bugs")