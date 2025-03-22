#Sawyer Wood, Battle Simulator stats and showing graphs

#Required libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
    character_csv = pd.read_csv('BattleSimulator/csvs/characters.csv')
    character_csv_statistics = character_csv.describe()
    print(f"\nFirst, before we show specific stats of {character['name']}, here are the general statistics:\n{character_csv_statistics}")

    move_on = input("\nEnter anything to continue.\n")

    print("\nNow for", character['description'])
    print("\nThe bar graph of their stats have been shown, close the window to move onto the next graph.")

    # Data for the bar graph
    categories = ["Health", "Strength", "Defense", "Speed", "Level", "Current XP"]
    values = [character["health"], character["strength"], character['defense'], character['speed'], character['level'], character['xp']]
    colors = ['crimson', 'lightcoral', 'lightgray', 'cornflowerblue', 'gold', 'limegreen']

    # Create the bar graph
    plt.bar(categories, values, color = colors)

    # Add title and labels
    plt.title(f'{character["name"]} Stats')
    plt.xlabel('Stat Type')
    plt.ylabel('Values')

    # Show the graph
    plt.show()

    print("\nClose this window to exit.")
    # Data for the pie chart
    labels = ['Health', 'Strength', 'Defense', 'Speed']
    sizes = [character["health"], character["strength"], character['defense'], character['speed']]
    colors = ['crimson', 'lightcoral', 'lightgray', 'cornflowerblue']

    # Create the pie chart
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

    # Add title
    plt.title(f'Stats distribution percentage for {character["name"]}')

    # Show the chart
    plt.show()
    return