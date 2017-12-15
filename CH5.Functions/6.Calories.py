print("Lets calculate where youre calories come from")

def Getter():
    fat = input("How much fat yod you eat per day g ?")
    carbs = input("How much Carbs are you eating per day g ? ")
    Calculator(fat,carbs)
    

def Calculator(fat,carbs):
    caloriesFromFat = fat * 9
    caloriesFromCarbs = carbs * 4
    totalCalories=caloriesFromCarbs+caloriesFromFat
    Sender(caloriesFromFat,caloriesFromCarbs,totalCalories)

def Sender(fattieCalories,carbieCalories,cal):
    print("Your fatty calorries",fattieCalories)
    print("Your Carby calories",carbieCalories)
    print("You ate a total of ",cal,"You shamless bastard go do some exercises !!!")

