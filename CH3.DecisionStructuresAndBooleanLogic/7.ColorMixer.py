
print("Lets mix some colors :) !!!")
print("Choose frome blue, red and yellow")
color1 = input("Please name the first color ")
color2 = input("Please name the second color ")

if ((color1 == "blue" and color2 == "red") or (color1 == "red" and color2 == "blue")):
    print("Your new color is PURPLE")
elif ((color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red")):
    print("Your new color is ORANGE")
elif ((color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue")):
    print("Your new color is GREEN")
else:
    print("You've typed in something wrong!!!")