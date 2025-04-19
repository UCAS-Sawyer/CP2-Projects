# Sawyer Wood, Geometry Calculator

from Rectangle import Rectangle
from Triangle import Triangle
from Circle import Circle

#This is the main function
def main():
    choice = input("\nWhat would you like to do, 1: Calculate Rectangle, 2: Calculate Triangle, 3: Calculate Circle, 4: Exit?\n")

    if choice == "1":
        Rectangle()
    elif choice == "2":
        Triangle()
    elif choice == "3":
        Circle()
    elif choice == "4":
        raise SystemExit
    else:
        print("\nThat is not an option.")
    
    main()

#Clearing Screen
print("\033[H\033[J")

main()