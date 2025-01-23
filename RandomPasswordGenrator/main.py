#Sawyer Wood, random password generator

#Importing random library and string library
import random
import string

#Required lists for creating the password
LowercaseLetters = [string.ascii_lowercase]
UppercaseLetters = [string.ascii_uppercase]
Numbers = [string.digits]
Symbols = [string.punctuation]

#Exception handling for ints
def intchecker(Inputx):
    try:
        Inputx = int(Inputx)
        return(Inputx)
    except:
        print("\nThat is not a valid input.")
        return None

#Exception handling for yes or no
def yesnointchecker(Inputx):
    if Inputx in ["1", "2"]:
        return(Inputx)
    else:
        print("\nThat is not a valid input.")
        return None

def generatepassword():
    Listtopickfrom = []
    #Asking for the paramiters for the password and checking that they are the correct inputs
    LenOPassword = intchecker(input("\nHow long do you want the password to be?\t"))
    if type(LenOPassword) == int:
        IncludeLowercase = yesnointchecker(input("\nDo you want to include lowercase letters? 1: Yes. 2: No\t"))
        if IncludeLowercase != None:
            IncludeUppercase = yesnointchecker(input("\nDo you want to include uppercase letters? 1: Yes. 2: No\t"))
            if IncludeUppercase != None:
                IncludeNumbers = yesnointchecker(input("\nDo you want to include numbers? 1: Yes. 2: No\t"))
                if IncludeNumbers != None:
                    IncludeSymbols = yesnointchecker(input("\nDo you want to include special characters? 1: Yes. 2: No\t"))
                    if IncludeSymbols != None:
                        if IncludeLowercase == "1":
                            Listtopickfrom.append(LowercaseLetters)
                        if IncludeUppercase == "1":
                            Listtopickfrom.append(UppercaseLetters)
                        if IncludeNumbers == "1":
                            Listtopickfrom.append(Numbers)
                        if IncludeSymbols == "1":
                            Listtopickfrom.append(Symbols)
                            #WORKING RIGHT HERE
                        for x in range(LenOPassword):
                            randomlist = random.choice(Listtopickfrom)
                            print(random.choice(randomlist))

                            


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