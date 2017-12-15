print("Enter your name middle name and surname")

fullName = input("And i'll print the initials\n")
initials = ""

nameString = fullName.split()
for name in nameString:
    initials += name[0]+"."
print(initials.upper())