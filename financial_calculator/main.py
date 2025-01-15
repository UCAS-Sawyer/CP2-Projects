#Sawyer Wood, Finacial Calculator

#---

#This is the financial calculator program that will have:
#How long it will take to save for a goal based on a weekly or monthly deposit
#Compound Interest Calculator 
#Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
#Sale Price Calculator (apply discounts to prices)
#Tip Calculator

#---

#Exception handling for floats
def floatchecker(inputx):
    try:
        #Turning it into the float and returning it
        inputx = float(inputx)
        return inputx
    except:
        #If it can't be turned into a float then it will return them back to the UI 
        print("\nThat is an invalid input.")

def saveingcalculator():
    #Asking if the person is going to pay weekly or monthly
    weeklyormonthly = input("\nDo you want the payments to be 1:Weekly or 2: Monthly?\t")
    #Checking if it is one of the options
    if weeklyormonthly not in ["1", "2"]:
        print("\nThat is not a valid input.")

    elif weeklyormonthly == "1":
        #Inputs for the needed variables & invalid input handling
        Income = floatchecker(input("\nWhat is your weekly income.\t"))
        if type(Income) == float:
            MoneySavedGoal = floatchecker(input("\nHow much money do you want to save?\t"))
            if type(MoneySavedGoal) == float:
                WeeklyDepositAmount =  floatchecker(input("\nHow much are you going to deposit each week.\t"))
                if type(WeeklyDepositAmount) == float:

                    #Making sure the amount is valid
                    if WeeklyDepositAmount > Income:
                        print("\nYou can not deposit that amount per week")
                    elif WeeklyDepositAmount <= 0:
                        print("\nYou aren't depositing anything.")
                    
                    else:
                        #Doing the math for the amount of weeks and printing the output
                        print("\nIt will take", MoneySavedGoal/WeeklyDepositAmount, "weeks.")

    elif weeklyormonthly == "2":
        #Inputs for the needed variables & invalid input handling
        Income = floatchecker(input("\nWhat is your monthly income.\t"))
        if type(Income) == float:
            MoneySavedGoal = floatchecker(input("\nHow much money do you want to save?\t"))
            if type(MoneySavedGoal) == float:
                MonthlyDepositAmount =  floatchecker(input("\nHow much are you going to deposit each month.\t"))
                if type(MonthlyDepositAmount) == float:

                    #Making sure the amount is valid
                    if MonthlyDepositAmount > Income:
                        print("\nYou can not deposit that amount per week")
                    elif MonthlyDepositAmount <=0:
                        print("\nYou aren't depositing anything.")       

                    else:
                        #Doing the math for the amount of months and printing the output
                        print("\nIt will take", MoneySavedGoal/MonthlyDepositAmount, "Months.")    

def InterestCalc():
    #Required inputs and exception handling
    AmountOMoney = floatchecker(input("\nWhat is the initial amount of money in the acount?\t"))
    if type(AmountOMoney) == float:
        InterestAmountPerYear = floatchecker(input("\nWhat is the interest you get per year(Percentage)?\t"))
        if type(InterestAmountPerYear) == float:
            AmountAddedEachYear = floatchecker(input("\nHow much are you going to add per year?\t"))
            if type(AmountAddedEachYear) == float:
                AmountInYears = floatchecker(input("\nHow many years do you want to calculate?\t"))
                if type(AmountInYears) == float:

                    InterestAmountPerYear = InterestAmountPerYear/100

                    #exception handling for the correct values
                    if InterestAmountPerYear <= 0:
                        print("\nYou can't have negative interest.")
                    
                    if AmountOMoney < 0:
                        print("\nThis calculator does not want a negative in the starting amount.")

                    AmountInYears = int(AmountInYears)
                    #Calculating the money based on the inputs for the amount of years inputed
                    for x in range(AmountInYears):
                        AmountOMoney = ((AmountOMoney + AmountAddedEachYear)*(1 + InterestAmountPerYear))
                    
                    AmountOMoney = round(AmountOMoney, 2)
                    
                    print(f"\nAfter {AmountInYears} years there would be ${AmountOMoney} in the acount.")
        
def BudgetAllocator():
    #Inputs for the needed variables & invalid input handling
    MonthlyIncome = floatchecker(input("\nWhat is your monthly income?\t"))

    if type(MonthlyIncome) == float:
        #Calculating all of the costs based on set percentages
        FoodPercentage = MonthlyIncome * 0.15
        HousingPercentage = MonthlyIncome * 0.3
        UtilitiesPercentage = MonthlyIncome * 0.15
        TransportationPercentage = MonthlyIncome * 0.15
        EntertainmentPercentage = MonthlyIncome * 0.05
        SavingsPercentage = MonthlyIncome - FoodPercentage - HousingPercentage -  UtilitiesPercentage - TransportationPercentage -  EntertainmentPercentage

        print(f"\nFrom your monthly income of ${MonthlyIncome} you need to allowcate 15% or ${FoodPercentage} to food, 30% or ${HousingPercentage} for housing, 15% or ${UtilitiesPercentage} for utilities, 15% or ${TransportationPercentage} for transportation, 5% or ${EntertainmentPercentage} for entertainment/activites and that leaves ${SavingsPercentage} left for savings.")


def SalePriceCalc():
    #Inputs for the needed variables & invalid input handling
    OriginalPrice = floatchecker(input("\nWhat is the initial price of the item?\t"))
    if type(OriginalPrice) == float:

        #PAsking for the input and checking for it to be valid
        ConstantorPercent = input("\nIs the discount a 1: flat number or 2: percent?\t")
        if type(ConstantorPercent) == float:
            #Checking weather ConstantorPercent is 1 or 2
            if ConstantorPercent in ["1"]:
                #Input and invalid checking
                Discountconstant = floatchecker(input("\nHow much is the item off in dollars?\t"))
                if type(Discountconstant) == float:

                    #Calculating the price minus the discount and printing it
                    print(f"The item will be ${OriginalPrice - Discountconstant}.")

            elif ConstantorPercent in ["2"]:
                #Input and invalid checking
                Discountpercent = floatchecker(input("\nWhat percent is it off?\t"))
                if type(Discountpercent) == float:

                    #Calculating the cost based on the discount percent
                    newamount = round(OriginalPrice * (1 - (Discountpercent/100)), 2)
                    #Printing the output
                    print(f"The item will be ${newamount}.")

            else:
                print("\nThat is not a valid input.")


def TipCalc():
    #Needed variables and valid checking
    CostOFood = floatchecker(input("\nWhat was the cost of the food after taxes?\t"))
    if type(CostOFood) == float:
        PercentageTip = floatchecker(input("\nWhat percentage do you want your tip to be?\t"))
        if type(PercentageTip) == float:

            #exception handling for value of the int
            if CostOFood <= 0:
                print("\nThis is an invalid amount for the cost of the food.")

            if PercentageTip <= 0:
                print("\nThis is an invalid amount for the percentage.")

            #Calculating the cost of the tip based on the percentage of the cost of the food.
            TipAmount = round((CostOFood * (PercentageTip / 100)), 2)
            #Printing the output
            print(f"\nA tip {PercentageTip}% of ${CostOFood} is ${TipAmount}.")

#This function is the Ui
def main():

    Decision = input("\nWhat do you want to do?(1:Calculate savings, 2:Coumpound Interest Calculator, 3:Budget Allocator, 4:Sale Price Calculator, 5:Tip Calculator, p:Exit)\t")

    #Checking all options for Decision
    if Decision == "1":
        saveingcalculator()

    elif Decision == "2":
        InterestCalc()
    
    elif Decision == "3":
        BudgetAllocator()

    elif Decision == "4":
        SalePriceCalc()

    elif Decision == "5":
        TipCalc()
    
    elif Decision == "p":
        #Stopping the program
        raise SystemExit

#Clearing Screen
print("\033[H\033[J")

while True:
    #Calling the UI
    main()
