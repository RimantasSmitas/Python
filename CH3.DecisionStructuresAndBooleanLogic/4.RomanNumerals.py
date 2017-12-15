
print("This program can help you transform number into Roman numerals")

number = int(input("type in your number from 1 to 10 "))
romanNumeral = ""

if(number == 1):
    romanNumeral = "I"
elif(number == 2):
    romanNumeral = "II"
elif(number == 3):
    romanNumeral = "III"
elif(number == 4):
    romanNumeral = "IV"
elif(number == 5):
    romanNumeral = "V"
elif(number == 6):
    romanNumeral = "VI"
elif (number == 7):
    romanNumeral = "VII"
elif(number == 8):
    romanNumeral = "VIII"
elif(number == 9):
    romanNumeral = "IX"
elif (number == 10):
    romanNumeral = "X"
else:
    print("you have typed in a wrong number number")

print(number,"in roman numerals is: ",romanNumeral)

