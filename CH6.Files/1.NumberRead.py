def main():
    file = open('numbers.txt', 'r')
    line = file.readline()
    while line != "":
        number = int(line)
        print(number)
        line = file.readline()
    file.close()
main()
