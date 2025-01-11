#Sawyer Wood, Finacial Calculator

#---

#This is the financial calculator program that will have:
#How long it will take to save for a goal based on a weekly or monthly deposit
#Compound Interest Calculator 
#Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
#Sale Price Calculator (apply discounts to prices)
#Tip Calculator

#---
while True:

    #Exception handling for floats

    def floatchecker(Inputx):
        try:
            inputx = float(inputx)
            return inputx
        except:
            print("\nThat is an invalid input.")
            return

    def saveingcalculator():
        
        weeklyormonthly = input("\nDo you want the payments to be 1:Weekly or 2: Monthly?\t")

        if weeklyormonthly not in ["1", "2"]:
            print("\nThat is not a valid input.")

        elif weeklyormonthly == "1":
            #Inputs for the needed variables & invalid input handling
            Income = input("\nWhat is your weekly income.\t")
            if type(floatchecker(Income)) == float:
                MoneySavedGoal = input("\nHow much money do you want to save?\t")
                if type(floatchecker(MoneySavedGoal)) == float:
                    WeeklyDepositAmount =  input("\nHow much are you going to deposit each week.\t")
                    if type(floatchecker(WeeklyDepositAmount)) == float:

                        #Making sure the amount is valid
                        if WeeklyDepositAmount > Income:
                            print("\nYou can not deposit that amount per week")
                        elif WeeklyDepositAmount <=0:
                            print("\nYou aren't depositing anything.")
                        
                        else:
                            print("\nIt will take", MoneySavedGoal/WeeklyDepositAmount, "weeks.")

        elif weeklyormonthly == "2":
            #Inputs for the needed variables & invalid input handling
            Income = input("\nWhat is your monthly income.\t")
            if type(floatchecker(Income)) == float:
                MoneySavedGoal = input("\nHow much money do you want to save?\t")
                if type(floatchecker(MoneySavedGoal)) == float:
                    MonthlyDepositAmount =  input("\nHow much are you going to deposit each month.\t")
                    if type(floatchecker(MonthlyDepositAmount)) == float:

                        #Making sure the amount is valid
                        if MonthlyDepositAmount > Income:
                            print("\nYou can not deposit that amount per week")
                        elif MonthlyDepositAmount <=0:
                            print("\nYou aren't depositing anything.")       

                        else:
                            print("\nIt will take", MoneySavedGoal/MonthlyDepositAmount, "Months.")    

    def InterestCalc():
        #Inputs for the needed variables
        AmountOMoney = input("\nWhat is the initial amount of money in the acount?\t")

        #Exception handling
        if type(floatchecker(AmountOMoney)) == float:
            InterestAmountPerYear = input("\nWhat is the interest you get per year(Percentage)?\t")
            if type(floatchecker(InterestAmountPerYear)) == float:
                AmountAddedEachYear = input("\nHow much are you going to add per year?\t")
                if type(floatchecker(AmountAddedEachYear)) == float:
                    AmountInYears = input("\nHow many years do you want to calculate?\t")
                    if type(floatchecker(AmountInYears)) == float:

                        InterestAmountPerYear = InterestAmountPerYear/100

                        #exception handling
                        if InterestAmountPerYear <= 0:
                            print("\nYou can't have negative interest.")
                        
                        if AmountOMoney < 0:
                            print("\nThis calculator does not want a negative in the starting amount.")

                        #Calculating Math
                        for x in range(AmountInYears):
                            AmountOMoney = ((AmountOMoney + AmountAddedEachYear)*(1 + InterestAmountPerYear))
                        
                        AmountOMoney = round(AmountOMoney, 2)
                        
                        print(f"\nAfter {AmountInYears} years there would be ${AmountOMoney} in the acount.")
            
    def BudgetAllocator():
        #Inputs for the needed variables & invalid input handling
        MonthlyIncome = input("\nWhat is your monthly income?\t")

        if type(floatchecker(MonthlyIncome)) == float:

            FoodPercentage = MonthlyIncome * 0.15
            HousingPercentage = MonthlyIncome * 0.3
            UtilitiesPercentage = MonthlyIncome * 0.15
            TransportationPercentage = MonthlyIncome * 0.15
            EntertainmentPercentage = MonthlyIncome * 0.05
            SavingsPercentage = MonthlyIncome - FoodPercentage - HousingPercentage -  UtilitiesPercentage - TransportationPercentage -  EntertainmentPercentage

            print(f"\nFrom your monthly income of ${MonthlyIncome} you need to allowcate 15% or ${FoodPercentage} to food, 30% or ${HousingPercentage} for housing, 15% or ${UtilitiesPercentage} for utilities, 15% or ${TransportationPercentage} for transportation, 5% or ${EntertainmentPercentage} for entertainment/activites and that leaves ${SavingsPercentage} left for savings.")


    def SalePriceCalc():
        print("dsafsa")


    def TipCalc():
        #Needed variables
        CostOFood = float(input("\nWhat was the cost of the food after taxes?\t"))
        if type(floatchecker(CostOFood)) == float:
            PercentageTip = input("\nWhat percentage do you want your tip to be?\t")
            if type(floatchecker(PercentageTip)) == float:

                #exception handling
                if CostOFood <= 0:
                    print("\nThis is an invalid amount for the cost of the food.")

                if PercentageTip <= 0:
                    print("\nThis is an invalid amount for the percentage.")

                #Math
                TipAmount = round((CostOFood * (PercentageTip / 100)), 2)
                print(f"\nA tip {PercentageTip}% of ${CostOFood} is ${TipAmount}.")

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

    main()