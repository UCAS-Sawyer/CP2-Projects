#Sawyer Wood, Word Counter Main

from word_counter_and_writer import word_counter

def relative_filepath_checker(filepath):
    try:
        with open(filepath, "r"):
            return True
    except FileNotFoundError:
        print("\nThat is not a valid filepath")
        return False

def checking_word_count():
    filepath = input("\nWhat is the relative file path?\n")
    filepath = filepath.replace("\\", "/")

    if relative_filepath_checker(filepath) == True:
        word_counter(filepath)

#This function is the Ui
def main():

    decision = input("\nWhat do you want to do?(1:Check Word Count, 2:Exit)\n")

    #Checking all options for Decision
    if decision == "1":
        checking_word_count()
    elif decision == "2":
        #Stopping the program
        raise SystemExit
    else:
        print("\nThat is not a valid input.")

#Clearing Screen
print("\033[H\033[J")

while True:
    #Calling the UI
    main()