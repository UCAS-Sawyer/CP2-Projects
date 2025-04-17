#Error handling

def floatchecker(number, TypeONumber):
    try:
        number = float(number)
        return number
    except:
        print("\nPlease enter a valid number.")
        number = floatchecker(input(f"\nRetry to enter the {TypeONumber}: "), TypeONumber)
        return number
