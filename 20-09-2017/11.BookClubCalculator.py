print("We're gonna count how many points for the purchased books you'll get")

bookNr = int(input("So how many books did you buy ? "))

if bookNr >= 8:
    promotionPionts = 60
elif bookNr >= 6:
    promotionPionts = 30
elif bookNr >= 4:
    promotionPionts = 15
elif bookNr >= 2:
    promotionPionts = 5
else:
    promotionPionts = 0

print("Congratualtions you have earned",promotionPionts,"points!")