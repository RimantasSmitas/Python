
print("Let's count some calories")

caloriesPerMinute = 4.2
caloriesPerWorkout = 0.0

for count in range (10,31,5):
    caloriesPerWorkout = count*caloriesPerMinute
    print("You have burned",caloriesPerWorkout,"Calories by working out for",count,"minutes")