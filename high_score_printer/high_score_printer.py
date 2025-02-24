#Sawyer Wood, Functions to print the top five highscores

import csv

highscores = []

with open("high_score_printer/highscores.csv") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        #Creating the dictionary
        item = {
            "name" : row[0],
            "highscore" : row[1]
        }

        #Adding the item
        highscores.append(item)

    sorted_by_score = sorted(highscores, key = lambda gamer: gamer["highscore"])
    print(sorted_by_score)

#EX: of lambda function
students = [
    {"Name" : 'Alice', 
     "Letter" : 'B', 
     "Age": 18},
     {"Name" : 'Alice', 
     "Letter" : 'B', 
     "Age": 17},
     {"Name" : 'Alice', 
     "Letter" : 'B', 
     "Age": 19}
]

# Sort by age (second element of each tuple)
sorted_by_age = sorted(students, key=lambda student: student["Age"])
#print(sorted_by_age)