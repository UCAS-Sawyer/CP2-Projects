#Sawyer Wood, random password generator

def intchecker(Inputx):
    try:
        Inputx = int(Inputx)
        return(Inputx)
    except:
        print("\nThat is not a valid input.")
        return None

def main():
    LenOPassword = intchecker(input("\nHow long do you want the password to be?\t"))

while True:
    main()