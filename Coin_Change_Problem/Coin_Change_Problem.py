#Sawyer Wood Coin Changer problem

def coin_change_main():
    currency = currency_type()

def currency_type():
    currencies = "1. US Dollar, 2. Euro, 3. Pound, 4. Japanese Yen"
    currency = None

    currecny_type_choice = input(f"\nWhich available currecny are you inputing? {currencies}\n")

    if currecny_type_choice == "1":
        currency = "USD"
    if currecny_type_choice == "1":
        currency = "USD"
    if currecny_type_choice == "1":
        currency = "USD"
    if currecny_type_choice == "1":
        currency = "USD"
    else:
        print("\nThat is not a valid input.")
        currency_type()
        return currency
    
    print(f"You have selected the currecy {currency}.")
    return currency

