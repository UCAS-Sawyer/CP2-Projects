#Sawyer Wood, To Do List

number_lines = 0

def number_of_lines(number_lines):
    with open("ToDoList/To_Do_List.txt", "r") as file:
        lines = file.readlines()
        number_lines = len(lines)
        return number_lines

def add_item(number_lines):
    with open("ToDoList/To_Do_List.txt", "a", newline= "") as file:
        item = input("\nWhat item would you like to add to your list?\n")
        file.write(f"{number_lines + 1}. {item}\n")
        print(f"\nItem |{item}| has been added to the list.")

def check_off(number_lines):
    print("Check Off ITEM")
    
def remove_item(number_lines):
    print("Remove ITEM")

def print_list():
    print("dsfakfdkjfdsa")

def main(number_lines):
    number_lines = number_of_lines(number_lines)

    choice = input("\nWhat would you like to do, 1: Add An Item, 2: Check Off An Item, 3: Remove An Item, 4: See List, 5: Exit\n")

    if choice == "1":
        add_item(number_lines)
    elif choice == "2":
        check_off(number_lines)
    elif choice == "3":
        remove_item(number_lines)
    elif choice == "4":
        print_list()
    elif choice == "5":
        raise SystemExit
    else:
        print("\nThat is not an option.")

#Clearing Screen
print("\033[H\033[J")

while True:
    main(number_lines)