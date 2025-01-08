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

Income = 0



def saveingcalculator(Income):
    MoneySavedGoal = input("How much money do you want to save?\t")
    WeeklyDepositAmount =  input("How much are you going to deposit each week.")
    if WeeklyDepositAmount > Income:
        print("You can not deposit that amount per week")
    elif WeeklyDepositAmount <=0:
        print("You aren't depositing anything.")