#Sawyer Wood, file with functions that check stuff

#Exception handling for ints
def intchecker(inputx):
    try:
        #Turning it into the int and returning it
        inputx = int(inputx)

        return inputx
    except:
        #If it can't be turned into a int then it will return them back to the UI 
        print("\nThat is an invalid input. Not an int")
        return None

#Checker for names
def name_checker(characters):
    name = input("\nWelcome to the character creator! Please enter the name of your character.\n")

    #Checking if the name is taken
    for player in characters:
        if player["name"] == name:
            print("\nThat name is already taken, please try again.")
            name_checker(characters)
        else:
            return name