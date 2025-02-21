#Sawyer Wood, To Do List

number_lines = 0

def intchecker(inputx):
    try:
        #Turning it into the int and returning it
        inputx = int(inputx)
        return inputx
    except:
        #If it can't be turned into a int then it will return them back to the UI 
        print("\nThat is an invalid input.")
        return None

def number_of_lines(number_lines):
    with open("ToDoList/To_Do_List.txt", "r") as file:
        lines = file.readlines()
        number_lines = len(lines)
        return number_lines

def add_item(number_lines):
    with open("ToDoList/To_Do_List.txt", "a", newline= "") as file:
        item = input("\nWhat item would you like to add to your list?\n")
        file.write(f"\n{number_lines + 1}. {item}")
        print(f"\nItem |{item}| has been added to the list.")

def check_off(number_lines):
    print("Check Off ITEM")
    
def remove_item(number_lines):
    with open("ToDoList/To_Do_List.txt", "w+", newline= "") as file:
        changed_file = file

        item_position_to_remove = intchecker(input("\nWhat item would you like to remove?(Give the number)\n"))
        if item_position_to_remove != None:
            for x in range(item_position_to_remove):
                print(changed_file)
                next(changed_file)

def print_list():
    with open("ToDoList/To_Do_List.txt", "r") as file:
        for line in file:
            line_trimed = line.strip()
            print(f"\n{line_trimed}")

def main(number_lines):
    number_lines = number_of_lines(number_lines)

    choice = input("\nWhat would you like to do, 1: Add An Item, 2: Check Off An Item, 3: Remove An Item, 4: See List, 5: Exit\n")

    if choice == "1":
        add_item(number_lines)
    elif choice == "2":
        check_off(number_lines)
    elif choice == "3":
        print_list()
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