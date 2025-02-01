#Sawyer Wood, morse code translator
EnglishToCode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

CodeToEnglish = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
    '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/',
    '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' ', ' ': ''
}

def encryptmessage():
    TranslatedMessage = ""
    #message to be translated
    Message = input("\nWhat is the message you would like to translate? \t")
    Message = Message.upper()
    #Translate letter by letter
    for x in Message:
        TranslatedMessage += EnglishToCode[x]
        TranslatedMessage += " "

    #Print translated message
    print(TranslatedMessage)

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
            #If the letter is in CodeToEnglish
            if x in CodeToEnglish:
                #Add the Translated verson
                TranslatedMessage += CodeToEnglish[x]
        #Add a space inbetween words
        TranslatedMessage += " "

    #Print the translated message
    print(TranslatedMessage)

def main():
    Choice = input("\nDo you want to translate into, 1. Morse Code, 2. English \t")

    if Choice == "1":
        encryptmessage()
    elif Choice == "2":
        decryptmessage()
    else:
        print("\nThat is an invalid inpout.")

main()