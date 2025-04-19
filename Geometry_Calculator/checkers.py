#Error handling

def floatchecker(number, TypeONumber):
    try:
        number = float(number)
        if number > 0:
            return number
        else:
            print("\nPlease enter a number greater than 0.")
            number = floatchecker(input(f"\nRetry to enter the {TypeONumber}: "), TypeONumber)
            return number
    except:
        print("\nPlease enter a valid number.")
        number = floatchecker(input(f"\nRetry to enter the {TypeONumber}: "), TypeONumber)
        return number

def int_checker(number): 
    try:
        number = int(number)
        if number > 0:
            return number
        else:
            print("\nPlease enter a number greater than 0.")
            number = int_checker(input("\nRetry to enter the number: "))
            return number
    except:
        print("\nPlease enter a valid integer.")
        number = int_checker(input("\nRetry to enter the number: "))
        return number

def unitchecker(unit):
    unit = unit.lower()
    units = ["mm", "cm", "m", "km", "in", "ft", "yd", "mi", "nmi", "au", "ly", "pc", "fathoms", "rods", "chains"]
    for x in units:
        if unit == x:
            return unit
        else:
            pass

    print("\nPlease enter a valid unit of measurement.")
    unit = unitchecker(input("\nRetry to enter the unit of measurement: "))
    return unit