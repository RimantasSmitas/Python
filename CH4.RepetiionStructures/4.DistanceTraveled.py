

speed = float(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))
print("Hours\t\tDistance Traveled")

for num in range (1,hours+1,1):
    distance = num * speed
    print(num,"\t\t\t",distance)