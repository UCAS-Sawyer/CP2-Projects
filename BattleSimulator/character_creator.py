#Sawyer Wood, Battle Simulator character creator

import csv

from checkers import intchecker
from checkers import name_checker
from checkers import stat_points_left_checker

#List of al the characters
characters = []

def player_list_creator():
    with open("BattleSimulator/characters.csv", "r") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            #Creating the dictionary

            player = {
                "name" : row[0],
                "health" : int(row[1]),
                "strength" : int(row[2]),
                "defense" : int(row[3]),
                "speed" : int(row[4])
            }
            characters.append(player)

        return


def character_creator():
    stat_points_left = 10
    health = 10
    strength = 1
    defense = 1
    speed = 1
    #Getting name
    name = name_checker(characters)

    #Printing info
    print("\nYou will now pick your stats for your character. \nThe Health base stat is 10 and all the other bases are 1. \nYou will only have 10 points to allowcate to the stats: \n\tHealth, Strength, Defense, and Speed. Choose Carefully!")
    
    #Getting the health stat and checking to make sure it is valid
    health = intchecker(input("\nHow many points will you allowcate to Health?\n"))

    if health != None:
        if 0 <= health and health <=stat_points_left:
            stat_points_left_checker(stat_points_left, health)
            
            #Getting the strength stat and checking to make sure it is valid
            strength = intchecker(input("\nHow many points will you allowcate to Health?\n"))

            if strength != None:
                if 0 <= strength and strength != stat_points_left:

                    stat_points_left_checker(stat_points_left, strength)
                    #Getting the strength stat and checking to make sure it is valid
                    strength = intchecker(input("\nHow many points will you allowcate to Health?\n"))
                else:
                    print("\nThat is an invalid input.(not a valid number of points)")
                    character_creation_main()
            else:
                print("\nThat is an invalid input.(not an int)")
                character_creation_main()
        else:
            print("\nThat is an invalid input.(not a valid number of points)")
            character_creation_main()
    else:
        print("\nThat is an invalid input.(not an int)")
        character_creation_main()


def character_creation_main():
    choice = input("\nDo you want to continue to create a character, 1. Yes, 2. No ?\n")
    if choice == "1":
        player_list_creator()
        character_creator()
    elif choice == "2":
        return
    else:
        print("\nThat is not an option.")