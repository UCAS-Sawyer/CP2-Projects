#Sawyer Wood Coin Changer problem, checkers

def float_checker(inputa, currency):
    try:
        inputa = float(inputa)
    except:
        print("\nThat is not a number, try again.")
        inputa = float_checker(input(f"\nHow much {currency} are you going to calculate?\n"), currency)
    return inputa