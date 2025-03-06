#Sawyer Wood, file with functions that check stuff

#Exception handling for ints
def intchecker(inputx):
    try:
        #Turning it into the int and returning it
        inputx = int(inputx)
        return inputx
    except:
        #If it can't be turned into a int then it will return them back to the UI 
        print("\nThat is an invalid input.")
        return None

#Checker for names
def name_checker(characters):
    name = input("\nWelcome to the character creator! Please enter the name of your character.\n")

    #Checking if the name is taken
    for player in characters:
        if player[0] == name:
            print("\nThat name is already taken, please try again.")
            name_checker()
        
    return name

#Checker for stat points left
def stat_points_left_checker(stat_points_left, new_stat):
    #Removing points that have been used
    stat_points_left -= new_stat

    #If all the points are used, exit
    if stat_points_left == 0:
        print("\nYou have used all of your points, the othe stats will be set to their base values.")
        character_writer_to_file()
    else:
        return