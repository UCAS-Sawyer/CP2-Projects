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

        #This is a tuple
        Item = (NameOfBook, NameOfAuthor, NumberOfPages)

        print(f"\nThe book has been added.")

        #Adding the item to the list
        Library.append(Item)

def RemoveItem(Library):
    #Necassary inputs and checking if it is in the library
    NameOfBook = input("\nWhat is the name of the book you would like to remove?\t")
    for item in Library:
        #Checking if the title of the book is in the library and removing it"
        if NameOfBook == item[0]:
            print("\n", item[0], "has been removed.")
            Library.remove(item)
        else:
            print("\nThat is not one of the titles of any of the books in the library.\t")

def SearchForItem(Library):
    found = False
    #Necassary inputs and valid checking
    AuthorOrTitle = input("\nDo you want to seach by 1: Author Name or 2: Book Title ?\t")
    
    if AuthorOrTitle == "1":
        #Necassary input
        AuthorName = input("\nWhat is the author's name?\t")
        for item in Library:
            #Checking if any of the books are by the author
            if AuthorName == item[1]:
                print(f"\nTitle: {item[0]}, Author's Name: {item[1]}, Number of Pages: {item[2]}")
                found = True
        if found == False:
            print("\nThere are no books by that author in here.")

    elif AuthorOrTitle == "2":
        #Necassary input
        BookTitle = input("\nWhat is the title of the book?\t")
        for item in Library:
            #Checking if any of the books have the title
            if BookTitle == item[0]:
                print(f"\nTitle: {item[0]}, Author's Name: {item[1]}, Number of Pages: {item[2]}")
                found = True
        if found == False:
            print("\nThere are no books with that title in here.")
    else:
        print("\nThat is not one of the options.")

def main():
    Disicion = input("\nDo you want to 1: Add an item, 2: Remove an item, 3: Search for an item, 4: Display Library, 5: Exit ? \t")

    if Disicion == "1":
        AddItem(Library)
    elif Disicion == "2":
        RemoveItem(Library)
    elif Disicion == "3":
        SearchForItem(Library)
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