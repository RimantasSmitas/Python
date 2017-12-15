
print("We'll calculate average rainfall")
years = int(input("Type in the number of years "))
totalRainfall = 0
months = 0

for year in range(1,years+1):
    for month in range(1,13):
        print("Type in the amount of rain for the ",month,"month of year ",year)
        rainfall = int(input())
        totalRainfall += rainfall
        months = months + 1

print("We have counted the data for ",months,"months")
print("total rainfall is",totalRainfall)
monthlyAverage = totalRainfall / (years*12)
print("Monthly average is ",format(monthlyAverage,".2f"))