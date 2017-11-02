hotdogsInAPackage = 10
bunsInAPackage = 8

print("Lets prepare for a hot dog cookout")
humanNumber = int(input("How many people will be attending? "))
hotdogsPerHuman = int(input("How many hotdogs per person? "))

hotdogsRequired = humanNumber*hotdogsPerHuman
bunsRequired = hotdogsRequired
hotdogPackages = hotdogsRequired // hotdogsInAPackage

if (hotdogPackages*hotdogsInAPackage-hotdogsRequired)!=0:
    hotdogPackages = hotdogPackages + 1
bunPackages = bunsRequired // bunsInAPackage
if (bunsRequired - bunPackages*bunsInAPackage)!=0:
    bunPackages = bunPackages + 1

leftoverHotdogs = hotdogPackages*hotdogsInAPackage-hotdogsRequired
leftoverBuns = bunPackages*bunsInAPackage-bunsRequired

print("\n")
print("You will require",hotdogPackages,"packs of hotdogs")
print("And",bunPackages,"packs of buns")
print("There will be",leftoverHotdogs,"leftover hot dogs")
print("And",leftoverBuns,"leftover buns")