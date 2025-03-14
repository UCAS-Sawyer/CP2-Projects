#Sawyer Wood, Battle Simulator fighting and battle sim

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
            print(f'You have chosen, {chosen_character["name"]}, to fight with.')
        else:
            print("\nThat character number does not exist, try again.")
            fighting_main()
            return
    else:
        fighting_main()
        return