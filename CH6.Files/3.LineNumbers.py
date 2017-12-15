

def main():
    name = input("Whats the name of the file you'd like to open? \n")
    file = open(name, 'r')
    number = 0
    for line in file:
        number +=1
        message = ""

        message = str(number) + line +","
        print(message)
    file.close()
main()


