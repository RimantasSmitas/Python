###             EXERCISE 13            ###

x = 7
stars = ""
while x > 0:
    y = x
    while y > 0:
        stars = stars + "*"
        y = y - 1
    print(stars)
    x = x - 1
    stars = ""

###             EXERCISE 14            ###

z = 6
gap = ""
startEnd = "#"
while z > 0:
    print(startEnd+gap+startEnd)
    gap = gap + " "
    z = z -1
