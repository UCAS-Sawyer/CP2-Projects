#Sawyer Wood Coin Changer problem

import csv

def coin_change_main():
    currency = currency_type()
    coins_and_bills = reading_csv()
    print(coins_and_bills)
    
    def currency_type():
        currencies = "1. US Dollar, 2. Euro, 3. Pound, 4. Japanese Yen"
        currency = None

        currecny_type_choice = input(f"\nWhich available currecny are you inputing? {currencies}\n")

        if currecny_type_choice == "1":
            currency = "USD"
        elif currecny_type_choice == "2":
            currency = "Euro"
        elif currecny_type_choice == "3":
            currency = "Pound"
        elif currecny_type_choice == "4":
            currency = "JYen"
        else:
            print("\nThat is not a valid input.")
            currency_type()
            return currency
        
        print(f"\nYou have selected the currecy {currency}.")
        return currency

    def reading_csv():
        #List of all the coins and bills
        coins_and_bills = []

        with open(f"Coin_Change_Problem\\csvs\\{currency}.csv", "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                #Creating the dictionary

                coin_or_bill = {
                    "name" : row[0],
                    "amount" : int(row[1]),
                }
                coins_and_bills.append(coin_or_bill)

            return coins_and_bills
