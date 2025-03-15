#Sawyer Wood, Battle Simulator fighting and battle sim

import csv
import random

from character_creator import player_list_creator
from checkers import intchecker

#The main for the fighting
def fighting_main():
    choice = input("\nDo you want to continue to battle, 1. Yes, 2. No ?\n")
    if choice == "1":
        characters = player_list_creator()
        battle_character(characters)
    elif choice == "2":
        return
    else:
        print("\nThat is not an option.")
        fighting_main()

def monster_list_creator(file_path):
    #List of all the characters
    monsters = []

    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            #Creating the dictionary

            monster = {
                "name" : row[0],
                "health" : int(row[1]),
                "strength" : int(row[2]),
                "defense" : int(row[3]),
                "speed" : int(row[4]),
                "xp" : int(row[5])
            }
            monsters.append(monster)

        return monsters

#choosing the character
def battle_character(characters):
    print("\nWhich character do you want to use?")
    character_number = 0

    #Printing all the characters
    for character in characters:
        character_number += 1
        print(f"{character_number}. Name: {character['name']}, Health: {character['health']}, Strength: {character['strength']}, Defense: {character['defense']}, Speed: {character['speed']}, Level: {character['level']}")
    
    #Choosing the character and error handling
    character_choice = intchecker(input("\nEnter the number of the character: "))

    if character_choice != None:
        if 1 <= character_choice and character_choice <= character_number:

            chosen_character = characters[character_choice - 1]
            print(f'\nYou have chosen, {chosen_character["name"]}, to fight with.')
            battle(chosen_character)
            return
        else:
            print("\nThat character number does not exist, try again.")
            fighting_main()
            return
    else:
        fighting_main()
        return
    
def battle(chosen_character):
    #Setting the monsters according to the character lvl
    if chosen_character["level"] >=0 and chosen_character["level"] <= 3:
        monsters = monster_list_creator("BattleSimulator/csvs/easy_monsters.csv")
        print(monsters)
    elif chosen_character["level"] >3 and chosen_character["level"] <= 8:
        monsters = monster_list_creator("BattleSimulator/csvs/medium_monsters.csv")
        print(monsters)
    else:
        monsters = monster_list_creator("BattleSimulator/csvs/hard_monsters.csv")
        print(monsters)

    #Checking if the monster is dead and doing lvl up stuff
    def monster_dead():
        nonlocal chosen_character, monster

        #Give the character xp
        chosen_character["xp"] += monster["xp"]
        #If the character has enough xp to level up they level up and gain a stat
        if chosen_character["xp"] >= chosen_character["level"] * 15:
            stats = ["health","strength","defense","speed"]
            
            chosen_character["xp"] -= chosen_character["level"] * 15
            chosen_character["level"] += 1

            lvlup_stat_change = random.choice(stats)
            chosen_character[lvlup_stat_change] += 2
            print(f"\nYou have leveled up! {lvlup_stat_change} is now {chosen_character[lvlup_stat_change]}.")
            print(f"\nYou have defeated the {monster['name']} and have gained {monster['xp']} xp, so you are now Level: {chosen_character['level']} and have {chosen_character['xp']} xp.")

            return lvlup_stat_change, chosen_character["xp"], chosen_character["level"], chosen_character[lvlup_stat_change]
        else:
            print(f"\nYou have defeated the {monster['name']} and have gained {monster['xp']} xp, so you are now Level: {chosen_character['level']} and have {chosen_character['xp']} xp.")
            return None
    
    #Picking which monster to fight
    monster = random.choice(monsters)

    #Setting current health to base health
    character_health = chosen_character["health"]

    #Deciding who goes first
    if chosen_character["speed"] > monster["speed"]:
        print("\nYou get to go first.")

        #While the monster is still alive
        while monster["health"] > 0:
            monster["health"] -= chosen_character["strength"] + 2
            print(f"\nYou attack the {monster['name']} and do {chosen_character['strength'] + 2} dmg to it.")
            
            if monster["health"] <= 0:
                if monster_dead() == None:
                    pass
                else:
                    lvlup_stat_change, xp, level, stat_change = monster_dead()

                    #Setting the stats to their new values
                    chosen_character["xp"] = xp
                    chosen_character["level"] = level
                    chosen_character[lvlup_stat_change] = stat_change
                    #WRITE THE CHARACTER AGAIN PLS
                    return
            else:
                print(f"That hit did not kill the {monster['name']}.")

    else:
        print(f"\nThe {monster['name']} gets to go first.")