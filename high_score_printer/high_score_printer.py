#Sawyer Wood, Functions to print the top five highscores

import csv
import fontstyle

file_path = "high_score_printer/highscores.csv"

#It requires the file path to be sent to it
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
        print("Rank    Name    Score")
        for x in sorted_by_score:
            player_number += 1
            if player_number <= 5:
                if player_number == 1:
                    print(fontstyle.apply(f"{player_number}\t{x["name"]}\t{x["highscore"]}", "underline/bold/Italic/yellow"))
                elif player_number == 2:
                    print(fontstyle.apply(f"{player_number}\t{x["name"]}\t{x["highscore"]}", "bold/Italic/green"))
                elif player_number == 3:
                    print(fontstyle.apply(f"{player_number}\t{x["name"]}\t{x["highscore"]}", "Italic/cyan"))
                elif player_number == 4:
                    print(fontstyle.apply(f"{player_number}\t{x["name"]}\t{x["highscore"]}", "purple"))
                elif player_number == 5:
                    print(fontstyle.apply(f"{player_number}\t{x["name"]}\t{x["highscore"]}", "red"))
            else:
                break
    #Back to where you came from
    return

high_score_printer_complexgame(file_path)