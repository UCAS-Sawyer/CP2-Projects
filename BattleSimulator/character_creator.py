#Sawyer Wood, Battle Simulator character creator

import csv

from checkers import intchecker
from checkers import name_checker

def player_list_creator():
    #List of all the characters
    characters = []

    with open("BattleSimulator/csvs/characters.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            #Creating the dictionary

            player = {
                "name" : row[0],
                "health" : int(row[1]),
                "strength" : int(row[2]),
                "defense" : int(row[3]),
                "speed" : int(row[4]),
                "level" : int(row[5])
            }
            characters.append(player)

        return characters

#Writing the character with all their stats onto the csv file
def character_writer_to_file(health, strength, defense, speed, name):
    with open("BattleSimulator/csvs/characters.csv", "a") as file:
        file.write(f"{name},{health},{strength},{defense},{speed},0\n")
        print(f"\nThe character {name} has been created.")
    return
    
#Creating the character
def character_creator(characters):
    stat_points_left = 10
    health = 10
    strength = 1
    defense = 1
    speed = 1

    #Error message
    not_valind_number = "\nThat is an invalid input.(not a valid number of points)"

    #Getting name
    name = name_checker(input("\nWelcome to the character creator! Please enter the name of your character.\n"), characters)
    print(f"\nThe name of your character is now {name}.")

    #Checker for stat points left
    def stat_points_left_checker(new_stat):
        #So I can modify stat_points_left
        nonlocal stat_points_left

        #Removing points that have been used
        stat_points_left -= new_stat

        #If all the points are used, exit
        if stat_points_left == 0:
            print("\nYou have used all of your points, the othe stats will be set to their base values.")
            character_writer_to_file(health, strength, defense, speed, name)
            return
        else:
            return stat_points_left

    #Printing info
    print("\nYou will now pick your stats for your character. \nThe Health base stat is 10 and all the other bases are 1. \nYou will only have 10 points to allowcate to the stats: \n\tHealth, Strength, Defense, and Speed. Choose Carefully!")
    
    #Getting the health stat and checking to make sure it is valid
    health_points = intchecker(input("\nHow many points will you allowcate to Health(It will increase the amount of health you have)?\n"))

    #Checking if everything is valid and if they have enough points
    if type(health_points) == int:
        if 0 <= health_points and health_points <=stat_points_left:
            health += health_points
            stat_points_left = stat_points_left_checker(health_points)
            if stat_points_left == None:
                return

            #Getting the strength stat and checking to make sure it is valid
            strength_points = intchecker(input(f"\nHow many points of your {stat_points_left} left will you allowcate to Strength(It will increase the amount of dmg you deal)?\n"))

            #Checking if everything is valid and if they have enough points
            if type(strength_points) == int:
                if 0 <= strength_points and strength_points <= stat_points_left:
                    strength += strength_points
                    stat_points_left = stat_points_left_checker(strength_points)
                    if stat_points_left == None:
                        return

                    #Getting the Defense stat and checking to make sure it is valid
                    defense_points = intchecker(input(f"How many points of your {stat_points_left} left will you allowcate to Defense(It will decrease the dmg you take)?\n"))

                    #Checking if everything is valid and if they have enough points
                    if type(defense_points) == int:
                        if 0 <= defense_points and defense_points <= stat_points_left:
                            defense += defense_points
                            stat_points_left = stat_points_left_checker(defense_points)
                            if stat_points_left == None:
                                return

                            #The rest of the points will go to speed
                            print(f"\nThe rest of your points will go to speed. The amount is {stat_points_left}")
                            if stat_points_left == 0:
                                character_writer_to_file(health, strength, defense, speed, name)
                                return
                            else:
                                speed += stat_points_left
                                character_writer_to_file(health, strength, defense, speed, name)
                                return
                        else:
                            print(not_valind_number)
                            return
                    else:
                        return
                else:
                    print(not_valind_number)
                    return
            else:
                return
        else:
            print(not_valind_number)
            return
    else:
        return
