
def main():
    print("Hello, tell me how much does it cost to replace your house")
    cost = float(input())
    suggestion  = insurance(cost)
    print("It's is a good idea to insure your house for at least ",suggestion,"money")

def insurance(cost):

    minInsurance = cost*0.8
    return minInsurance


main()