print("Global warming!!!")
print("We need to prepare for it, the sea is rising 1.6 mm per year")
print("If this keeps up the see level will rise")
currentYear = 2017
seaLevelRise = 0.0

for x in range (0,25):
    seaLevelRise = seaLevelRise + 1.6
    currentYear = currentYear + 1
    print(format(seaLevelRise,".2f"),"mm by the year ",currentYear)

