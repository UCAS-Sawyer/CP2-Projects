#Sawyer Wood Movie Recommender

import csv

movies = []

#Creating a list of dictionaries of each item
with open("MovieRecommender/Movies list.csv") as file:
    csvReader = csv.reader(file)
    next(csvReader)
    for row in csvReader:
        item = {
            "Title" : row[0],
            "Director" : row[1],
            "Genre" : row[2],
            "Rating" : row[3],
            "Length (min)" : row[4],
            "Notable Actors" : row[5]
        }

        movies.append(item)

def PrintMovieTitles(movies):
    movieTitles = []
    for item in movies:
        movieTitles.append(item["Title"])

    print(movieTitles)


def main():
    choice = input("\nWhat would you like to do? 1: See All Movie Titles, 2: Search, 3: See All Information, 4: Exit\n")
    if choice == "1":
        PrintMovieTitles(movies)
    elif choice == "4":
        raise SystemExit

while True:
    main()