#Sawyer Wood, Reading File Notes

import csv

#Option 1
#with open("Notes/test.txt", "r") as file:
#    content = file.read()
#    print(content)


#Option 2
#file = open("Notes/test.txt", "r").read()
#
#print(file)

users = {}

with open("Notes/user_info.csv") as file:
    csvReader = csv.reader(file)
    next(csvReader)
    for row in csvReader:
        users.update({row[0] : row[1]})

print(users)