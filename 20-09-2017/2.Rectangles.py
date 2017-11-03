print("Hello human\nI can calculate the area of two rectangles\nand tell which one is bigger:D ")

lenght1 = float(input("type in the lenght of rectangle nr.1 "))
width1 = float(input("type in the width of rectangle nr.1 "))
lenght2 = float(input("type in the lenght of rectangle nr.2 "))
width2 = float(input("type in the width of rectangle nr.2 "))

area1 = lenght1*width1
area2 = lenght2*width2

print("First rectangle area is equal to:",area1,"square units")
print("Second rectangle area is equal to:",area2,"square units")

if (area1==area2):
    print("Your rectangles are the same size")
elif(area1>area2):
    print("The first rectangle is bigger")
else:
    print("The second rectangle is bigger")