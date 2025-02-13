#Sawyer Wood Movie Recommender

import csv

movies = []

#Creating a list of dictionaries of each item
with open("MovieRecommender/Movies list.csv") as file:
    csvReader = csv.reader(file)
    next(csvReader)
    for row in csvReader:
        item = {
            "Title" : row[0].lower(),
            "Director" : row[1].lower(),
            "Genre" : row[2].lower(),
            "Rating" : row[3].lower(),
            "Length (min)" : row[4].lower(),
            "Notable Actors" : row[5].lower()
        }

        movies.append(item)

def PrintMovieTitles(movies):
    movieTitles = []
    for item in movies:
        movieTitles.append(item["Title"])

    print(movieTitles)

def Search(movies):
    print("\nWorkInProgress!")

def main():
    choice = input("\nWhat would you like to do? 1: See All Movie Titles, 2: Search, 3: See All Information, 4: Exit\n")
    if choice == "1":
        PrintMovieTitles(movies)
    elif choice == "2":
        Search(movies)
    elif choice == "3":
        print(movies)
    elif choice == "4":
        raise SystemExit
    else:
        print("\nThat is not a valid option.")

while True:
    main()