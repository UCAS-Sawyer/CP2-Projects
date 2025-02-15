#Sawyer Wood Movie Recommender

import csv

movies = []

#Creating a dictionary for each item and then storing it in a list
with open("MovieRecommender/Movies list.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        item = {
            "Title" : row[0].lower(),
            "Director" : row[1].lower(),
            "Genre" : row[2].lower(),
            "Rating" : row[3].lower(),
            "Length (min)" : row[4].lower(),
            "Notable Actors" : row[5].lower()
        }

        movies.append(item)

#Exception handling for ints
def intchecker(inputx):
    try:
        #Turning it into the int and returning it
        inputx = int(inputx)
        return inputx
    except:
        #If it can't be turned into a int then it will return them back to the UI 
        print("\nThat is an invalid input.")
        return None

def print_movie_titles(movies):
    movie_titles = []
    for item in movies:
        movie_titles.append(item["Title"])

    print(movie_titles)

def filters_function():
    filters = []

    while True:
        filter_pair = []
        filter_choice = input("\nWhat do you want you first filter to be, 1: Genre, 2: Directors, 3: Length, 4: Actors, 5: Move on\n")
        filter_choice = filter_choice.strip()

        if filter_choice == "1":
            filter = "Genre"
        elif filter_choice == "2":
            filter = "Director"
        elif filter_choice == "3":
            filter = "Length (min)"
        elif filter_choice == "4":
            filter = "Notable Actors"  
        elif filter_choice == "5":
            break
        else:
            print("\nThat is not an option.")
            continue

        filter_data = input(f"\nWhat {filter} do you want to be recomended?\n").lower()
        filter_data = filter_data.strip()

        if filter == "Lenght (min)":
            intchecker = intchecker(filter_data)
            if intchecker == None:
                continue
        
        filter_pair.append(filter)
        filter_pair.append(filter_data)
        filters.append(filter_pair)

    return filters

def search(movies):
    filters = filters_function()


def main():
    choice = input("\nWhat would you like to do? 1: See All Movie Titles, 2: Get Recomendations, 3: See All Information, 4: Exit\n")
    choice = choice.strip()
    if choice == "1":
        print_movie_titles(movies)
    elif choice == "2":
        search(movies)
    elif choice == "3":
        print(movies)
    elif choice == "4":
        raise SystemExit
    else:
        print("\nThat is not a valid option.")

while True:
    main()