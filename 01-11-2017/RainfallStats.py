print("We'll calculate average rainfall")
years = int(input("Type in the number of years "))
totalRainfall = []
yearly  = 0.0
total = 0.0

for year in range(1,years+1):
    for month in range(1,13):
        print("Type in the amount of rain for the ",month,"month of year ",year)
        rainfall = int(input())
        totalRainfall.append(rainfall)


print("total rainfall is",totalRainfall)

for year in range(1,years+1):

    for monthe in range(1,13):
        yearly += totalRainfall[year*monthe-1]

    ##print("For the year",year," the total is: ",yearly)
    total +=yearly
print("The total is: ",total)
monthlyAverage = total / (years*12)
print("Monthly average is ",format(monthlyAverage))