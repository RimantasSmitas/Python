print("Hello human, I shall classify you by age")
print("How long has it been from your manufactory date in years?")

age = int(input())

if (age<=1):
    print("You are just an infant litle human\nHow can you read this at all???")
elif(age>1 and age<13):
    print("I classify you as a child human")
elif(age>13 and age<20):
    print("I classify you as a teenager human")
else:
    print("You're an adult!\n please dont kill me human")