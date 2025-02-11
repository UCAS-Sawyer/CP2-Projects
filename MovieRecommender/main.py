#Sawyer Wood Movie Recommender

import csv

movies = []

#Creating a list of dictionaries of each item
with open("MovieRecommender/Movies list.csv") as file:
    csvReader = csv.reader(file)
    next(csvReader)
    for row in csvReader:
        item = {}
        item.update({"Title" : row[0]})
        item.update({"Director" : row[1]})
        item.update({"Genre" : row[2]})
        item.update({"Rating" : row[3]})
        item.update({"Length (min)" : row[4]})
        item.update({"Notable Actors" : row[5]})
        movies.append(item)

print(movies)