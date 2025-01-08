#Sawyer Wood, Finacial Calculator

#---

#This is the financial calculator program that will have:
#How long it will take to save for a goal based on a weekly or monthly deposit
#Compound Interest Calculator 
#Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
#Sale Price Calculator (apply discounts to prices)
#Tip Calculator

#---

def main():
    pass

def saveingcalculator():

    #Inputs for the needed variables
    Income = input("What is your weekly income.")
    MoneySavedGoal = input("How much money do you want to save?\t")
    WeeklyDepositAmount =  input("How much are you going to deposit each week.")

    #Making sure the amount is valid
    if WeeklyDepositAmount > Income:
        print("You can not deposit that amount per week")
    elif WeeklyDepositAmount <=0:
        print("You aren't depositing anything.")
    
    print("It will take", MoneySavedGoal/WeeklyDepositAmount)

Desiction = input("What do you want to do?(1:Calculate savings, 2:Coumpound Interest Calculator, 3:Budget Allocator, 4:Sale Prive Calculator, 5:Tip Calculator)")