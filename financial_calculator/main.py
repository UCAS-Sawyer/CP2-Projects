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


    def saveingcalculator():

        #Inputs for the needed variables
        Income = int(input("\nWhat is your weekly income.\t"))
        MoneySavedGoal = int(input("\nHow much money do you want to save?\t"))
        WeeklyDepositAmount =  int(input("\nHow much are you going to deposit each week.\t"))

        #Making sure the amount is valid
        if WeeklyDepositAmount > Income:
            print("\nYou can not deposit that amount per week")
        elif WeeklyDepositAmount <=0:
            print("\nYou aren't depositing anything.")
        
        print("\nIt will take", MoneySavedGoal/WeeklyDepositAmount, "weeks.")

    def InterestCalc():
        #Inputs for the needed variables
        AmountOMoney = int(input("\nWhat is the initial amount of money in the acount?\t"))
        InterestAmountPerYear = int(input("\nWhat is the interest you get per year(Percentage)?\t"))
        AmountAddedEachYear = int(input("\nHow much are you going to add per year?\t"))
        AmountInYears = int(input("\nHow many years do you want to calculate\t"))

        InterestAmountPerYear = InterestAmountPerYear/100

        #exception handling
        if InterestAmountPerYear <= 0:
            print("You can't have negative interest.")
        
        if AmountOMoney < 0:
            print("This calculator does not want a negative in the starting amount.")

        #Calculating Math
        for x in range(AmountInYears):
            AmountOMoney = ((AmountOMoney + AmountAddedEachYear)*(1 + InterestAmountPerYear))
        
        print(f"After {AmountInYears} years there would be {AmountOMoney} in the acount.")
            
    def BudgetAllocator():
        print("dsafgdsahfgsafdsafdrkugdsafdgeraesdlufrva")

    def SalePriceCalc():
        print("dsafsa")

    def TipCalc():
        #Needed variables
        CostOFood = int(input(""))

    def main():

        Decision = input("\nWhat do you want to do?(1:Calculate savings, 2:Coumpound Interest Calculator, 3:Budget Allocator, 4:Sale Prive Calculator, 5:Tip Calculator, p:Exit)\t")

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