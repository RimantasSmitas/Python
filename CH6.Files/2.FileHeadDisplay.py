def main():

    file = open('sample.txt', 'r')
    line = file.readline()
    for x in range(5):
        print(line)
        line = file.readline()
    file.close()
main()
