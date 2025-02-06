#Sawyer Wood, Personal library Program

#Needs a set or a tuple somewhere.

library = []

def intchecker(inputx):
    try:
        inputx = int(inputx)
        return(inputx)
    except:
        print("\nThat is not a valid input.")
        return None

def AddItem(library):
    #Necassary inputs  and invalid checking
    nameOfBook = input("\nWhat is the name of the book?\t")
    nameOfAuthor = input("\nWhat is the name of the author?\t")
    numberOfPages = intchecker(input("\nHow many pages does it have?\t"))
    if numberOfPages != None:
        yearPublished = intchecker(input("\nWhat year was the book published?\t"))
        if yearPublished != None:
            item = {
                "Name" : nameOfBook, 
                "Author" : nameOfAuthor, 
                "#Pages" : numberOfPages,
                "Year" : yearPublished
                }

            print(f"\nThe book has been added.")

            #Adding the item to the list
            library.append(item)

def RemoveItem(library):
    #Necassary inputs and checking if it is in the library
    nameOfBook = input("\nWhat is the name of the book you would like to remove?\t")
    for item in library:
        #Checking if the title of the book is in the library and removing it"
        if nameOfBook == item["Name"]:
            print("\n", item["Name"], "has been removed.")
            library.remove(item)
        else:
            print("\nThat is not one of the titles of any of the books in the library.\t")

def SearchForItem(library):
    found = False
    #Necassary inputs and valid checking
    authorOrTitle = input("\nDo you want to seach by 1: Author Name or 2: Book Title ?\t")
    
    if authorOrTitle == "1":
        #Necassary input
        authorname = input("\nWhat is the author's name?\t")
        for item in library:
            #Checking if any of the books are by the author
            if authorname == item["Author"]:
                print(f"\nTitle: {item["Name"]}, Author's Name: {item["Author"]}, Number of Pages: {item["#Pages"]}, Year Published: {item["Year"]}")
                found = True
        if found == False:
            print("\nThere are no books by that author in here.")

    elif authorOrTitle == "2":
        #Necassary input
        bookTitle = input("\nWhat is the title of the book?\t")
        for item in library:
            #Checking if any of the books have the title
            if bookTitle == item["Name"]:
                print(f"\nTitle: {item["Name"]}, Author's Name: {item["Author"]}, Number of Pages: {item["#Pages"]}, Year Published: {item["Year"]}")
                found = True
        if found == False:
            print("\nThere are no books with that title in here.")
    else:
        print("\nThat is not one of the options.")

def PrintingLbrary(library):
    printingStuff = ""
    printingAuthors = set()
    disicion = input("\nDo you want to 1: Display Everything, 2: Display Only Book Names, 3: Display Only Authors? \t")

    if disicion == "1":
        print("\n", library)
    elif disicion == "2":
        for book in library:
            printingStuff += book["Name"]
        print([printingStuff])
    elif disicion == "3":
        for book in library:
            printingAuthors.add(book["Author"])
        print(printingAuthors)
    else:
        print("\nThat is not an option.")
    

def main():
    disicion = input("\nDo you want to 1: Add an item, 2: Remove an item, 3: Search for an item, 4: Display library, 5: Exit ? \t")

    if disicion == "1":
        AddItem(library)
    elif disicion == "2":
        RemoveItem(library)
    elif disicion == "3":
        SearchForItem(library)
    elif disicion == "4":
        PrintingLbrary(library)
    elif disicion == "5":
        raise SystemExit
    else:
        print("\nThat is not one of the options.")

#Clearing Screen
print("\033[H\033[J")
print("\nWelcome to the Personal library Program(PLP)")

while True:
    main()