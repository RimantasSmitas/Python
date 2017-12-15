print("Write the number of seconds, and im gonna say how many minutes, hours or days that is")

initialSeconds = int(input())
seconds = initialSeconds
minutes = int()
hours = int()
days = int()

#Calculate the number of days
while seconds >= 86400:
    seconds = seconds - 86400
    days = days + 1
#Calculate the number of hours
while seconds >= 3600:
    seconds =seconds - 3600
    hours = hours + 1
#Calculate the number of minutes
while seconds >= 60:
    seconds = seconds - 60
    minutes = minutes +1

print(initialSeconds,"Is equal to:",days,"days",hours,"hours,",minutes,"minutes and",seconds,"seconds")

