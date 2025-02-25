#Sawyer Wood, Functions to print the top five highscores

import csv

file_path = "high_score_printer/highscores.csv"

def high_score_printer_complexgame(file_path):

    #Clearing Screen
    print("\033[H\033[J")

    highscores = []
    player_number = 0

    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            #Creating the dictionary
            item = {
                "name" : row[0],
                "highscore" : int(row[1])
            }

            #Adding the item
            highscores.append(item)
            #sorting it by score
        sorted_by_score = sorted(highscores, key = lambda gamer: gamer["highscore"], reverse = True)

        #Printing all the scores with the names and ranks
        print("Rank    Name     Score")
        for x in sorted_by_score:
            player_number += 1
            if player_number <= 5:
                print(f"{player_number}\t{x["name"]}\t {x["highscore"]}")
            else:
                break
    #Back to where you came from
    return

high_score_printer_complexgame(file_path)