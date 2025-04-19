# Sawyer Wood, Geometry Calculator

from Rectangle import Rectangle
from Triangle import Triangle
from Circle import Circle
from Compare import compare_shapes

#This is the main function
def main():
    choice = input("\nWhat would you like to do, 1: Calculate Rectangle, 2: Calculate Triangle, 3: Calculate Circle, 4: Compare Shapes, 5: Exit?\n")

    if choice == "1":
        Rectangle()
    elif choice == "2":
        Triangle()
    elif choice == "3":
        Circle()
    elif choice == "4":
        compare_shapes()
    elif choice == "5":
        raise SystemExit
    else:
        print("\nThat is not an option.")
    
    main()

#Clearing Screen
print("\033[H\033[J")

main()