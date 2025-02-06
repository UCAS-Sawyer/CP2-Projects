#Sawyer Wood, morse code translator

English = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '?', '/', '-', '(', ')', '/', '!', ' ']

Code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-', '/', '-.-.--', ' ']

def encryptmessage():
    TranslatedMessage = ""
    #message to be translated
    Message = input("\nWhat is the message you would like to translate? \t")
    Message = Message.upper()
    #Translate letter by letter
    for x in Message:
        if x == " ":
            TranslatedMessage += " / "
        else:
            indexOfx = English.index(x)
            TranslatedMessage += Code[indexOfx]
            TranslatedMessage += " "

    #Print translated message
    print("\n", TranslatedMessage)

def decryptmessage():
    TranslatedMessage = ""
    #message to be translated
    Message = input("\nWhat is the message you would like to translate? !MorseCode Only! \t")

    #Breaking the words where the "/" is
    Words = Message.split("/")
    #For each word in words
    for Word in Words:
        #Spliting the word into letters
        Letters = Word.split(" ")
        #For each letter in Letters
        for x in Letters:
            #If the letter is in Code
            if x in Code:
                #Add the Translated verson
                indexOfx = Code.index(x)
                TranslatedMessage += English[indexOfx]

        #Add a space inbetween words
        TranslatedMessage += " "

    #Print the translated message
    print("\n", TranslatedMessage)

def main():
    Choice = input("\nDo you want to translate into, 1. Morse Code, 2. English, 3. Exit  \t")

    if Choice == "1":
        encryptmessage()
    elif Choice == "2":
        decryptmessage()
    elif Choice == "3":
        raise SystemExit
    else:
        print("\nThat is an invalid inpout.")

#Clearing Screen
print("\033[H\033[J")

while True:
    main()