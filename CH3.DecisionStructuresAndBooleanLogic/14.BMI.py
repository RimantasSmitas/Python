print("Let's calculate your BMI\n")

weight = input("Please enter your weight in pounds\n")
height = input("Please enter your height in inches\n")

bmi = weight * 703/height*height

if bmi > 25:
    print("Your BMI is",bmi,"\nYou are overweight")
elif bmi >18.5:
    print("Your BMI is",bmi,"\nYou are optimal weight")
else:
    print("Your BMI is",bmi,"\nYou are underweight")