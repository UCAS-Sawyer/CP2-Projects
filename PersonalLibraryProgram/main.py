#Sawyer Wood, Personal Library Program

#Needs a set or a tuple somewhere.

Library = []

def intchecker(Inputx):
    try:
        Inputx = int(Inputx)
        return(Inputx)
    except:
        print("\nThat is not a valid input.")
        return None

def AddItem(Library):
    #Necassary inputs  and invalid checking
    NameOfBook = input("\nWhat is the name of the book?\t")
    NameOfAuthor = input("\nWhat is the name of the author?\t")
    NumberOfPages = intchecker(input("\nHow many pages does it have?\t"))
    if NumberOfPages != None:

        Item = {
            "Title" : NameOfBook, 
            "Author" : NameOfAuthor, 
            "Pages" : NumberOfPages
            }

        print(f"\nThe item has been added.")

        #Adding the item to the list
        Library.append(Item)

def RemoveItem(Library):
    #Necassary inputs  and invalid checking
    NameOfBook = input("\nWhat is the name of the book you would like to remove?\t")
    for item in Library:
        #Checking if the title of the book is in the library and removing it"
        if NameOfBook == item["Title"]:
            print("\n", item["Title"], "has been removed.")
            Library.remove(item)
        else:
            print("\nThat is not one of the titles of any of the books in the library.\t")

def SearchForItem():
    print("\nNot ready yet.")


def main():
    Disicion = input("\nDo you want to 1: Add an item, 2: Remove an item, 3: Search for an item, 4: Display the library, 5: Exit ? \t")

    if Disicion == "1":
        AddItem(Library)
    elif Disicion == "2":
        RemoveItem(Library)
    elif Disicion == "3":
        SearchForItem()
    elif Disicion == "4":
        print("\n", Library)
    elif Disicion == "5":
        raise SystemExit
    else:
        print("\nThat is not one of the options.")

#Clearing Screen
print("\033[H\033[J")
print("\nWelcome to the Personal Library Program(PLP)")

while True:
    main()