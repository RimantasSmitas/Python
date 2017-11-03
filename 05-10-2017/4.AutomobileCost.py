
class getCosts:
    def getLoan():
        loanPayment = float(input("How much do you pay per month to the bank for your car? "))
        return loanPayment
    def getInsurance():
        insurance = float(input("How much are you paying for the cars' insurance per month? "))
        return insurance
    def getGas():
        gas = float(input("How much are you paying for the cars' gas per month? "))
        return gas
    def getOil():
        oil = float(input("How much are you paying for the cars' oil per month? "))
        return oil
    def getTires():
        tires = float(input("How much are you paying for the cars' tires per month? "))
        return tires
    def getMaintenance():
        maintenance = float(input("How much are you paying for the cars' maintenece per month? "))
        return maintenance


def yearlyExpense(loan,insurance,gas,oil,tires,maintenance):
    monthlyCosts = float(loan + insurance + gas + oil + tires + maintenance)
    costsPerYear = monthlyCosts * 12
    return  costsPerYear


def main():
    yearlyCost = yearlyExpense(getCosts.getLoan(),getCosts.getInsurance(),getCosts.getGas(),getCosts.getOil(),getCosts.getTires(),getCosts.getMaintenance())
    print(yearlyCost)

main()