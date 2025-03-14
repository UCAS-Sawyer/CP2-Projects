#Sawyer Wood, Battle Simulator main
from character_creation_main import character_creation_main
from fighting import fighting_main

#This is the main function
def main():
    choice = input("\nWhat would you like to do, 1: Create A Character, 2: Fight With A Character, 3: Exit\n")

    if choice == "1":
        character_creation_main()
    elif choice == "2":
        fighting_main()
    elif choice == "3":
        raise SystemExit
    else:
        print("\nThat is not an option.")
    
    main()

#Clearing Screen
print("\033[H\033[J")

main()