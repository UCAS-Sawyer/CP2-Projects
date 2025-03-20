#Sawyer Wood, Battle Simulator stats and showing graphs

#Required libraries
import matplotlib.pyplot as plt
import numpy as np

from character_creator import player_list_creator
from checkers import intchecker

def stats_main():
    character_number = 0

    #Getting a list of all the characters
    character_list = player_list_creator()
    print("\nWhich character do you want to se their stats?")

    #Printing all the characters
    for character in character_list:
        character_number += 1
        print(f"{character_number}. Name: {character['name']}")

    #Choosing the character and error handling
    character_choice = intchecker(input("\nEnter the number of the character: "))

    if character_choice != None:
        if 1 <= character_choice and character_choice <= character_number:

            chosen_character = character_list[character_choice - 1]
            print(f'\nYou have chosen, {chosen_character["name"]}, to see their stats.')
            stats(chosen_character)
            return
        else:
            print("\nThat character number does not exist, try again.")
            stats_main()
            return
    else:
        stats_main()
        return
    
#Not really working
def stats(character):
    plt.style.use('_mpl-gallery')

    # make data:
    x = 0.5 + np.arange(6)
    y = [character["health"], character["strength"], character['defense'], character['speed'], character['level'], character['xp']]

    # plot
    fig, ax = plt.subplots()

    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 6),
        ylim=(0, 100), yticks=np.arange(1, 100))

    plt.bar_label = (["Health", "Strength", "Defense", "Speed", "Level", "Current XP"])
    ax.set_ylabel('Stat value')
    ax.set_title(f'Stats for {character["name"]}')

    plt.show()

    print("\nThe stats have been shown.")
    return