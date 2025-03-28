#Sawyer Wood Coin Changer problem, checkers

def float_checker(inputa, currency):
    try:
        inputa = float(inputa)
        return inputa
    except:
        print("\nThat is not a number, try again.")
        inputa = input(f"\nHow much {currency} are you going to calculate?\n")
        float_checker(inputa, currency)
        print("yoolo")
        return inputa