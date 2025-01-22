#Sawyer Wood, random password generator

def intchecker(Inputx):
    try:
        Inputx = int(Inputx)
        return(Inputx)
    except:
        print("\nThat is not a valid input.")
        return None

def yesnointchecker(Inputx):
    if Inputx in ["1", "2"]:
        return(Inputx)
    else:
        print("\nThat is not a valid input.")
        return None

def generatepassword():
    #Asking for the paramiters for the password and checking that they are the correct inputs
    LenOPassword = intchecker(input("\nHow long do you want the password to be?\t"))
    if type(LenOPassword) == int:
        IncludeLowercase = yesnointchecker(input("\nDo you want lowercase letters in your password 1: Yes. 2: No\t"))
        if IncludeLowercase != None:
            IncludeUppercase = yesnointchecker(input("\nDo you want to include uppercase letters? 1: Yes. 2: No\t"))
            if IncludeUppercase != None:
                IncludeNumbers = yesnointchecker(input("\nDo you want to include numbers? 1: Yes. 2: No\t"))
                if IncludeNumbers != None:
                    IncludeSymbols = yesnointchecker(input("\nDo you want to include special characters? 1: Yes. 2: No\t"))
                    if IncludeSymbols != None:
                        print("It all worked.")

def main():
    #Choice between generate password and quit
    choice = input("\nWhat do you want to do? 1: Generate Password, 2: Quit\t")

    if choice == "1":
        generatepassword()
    elif choice == "2":
        raise SystemExit
    else:
        print("\nThat is not a valid input.")

#Clearing Screen
print("\033[H\033[J")

while True:
    main()