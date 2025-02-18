#Sawyer Wood, Notes for writing to text files
"""

r = to read the file
w = write on the file(replaces old contents)
w+ = read and write
a = append (adds to the file, doesn't delete them) (It will create the file if it doesn't exist)
x - create a file
a+ = append and read

"""
#with open("Notes/test.txt", "a") as file:
#    file.write("\nRandom things and stuff")


import csv


data = [
    {"username" : "MEME", "colour" : "POIPLE"}
]




with open("Notes/user_info.csv", "a", newline= "") as file:
    fieldnames = ["username", "colour"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open("Notes/user_info.csv", "r") as file:

    reader = csv.reader(file)
    for row in reader:
        print(f"username: {row[0]}           favcolour: {row[1]}\n------------------")