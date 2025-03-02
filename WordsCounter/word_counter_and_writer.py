#Sawyer Wood, Word Counter, Counter Function

def word_counter(filepath):
    with open(filepath, "r") as file:
        all_words = []
        lines = file.readlines()
        #Getting all the words into a list
        for line in lines:
            words = line.split(" ")
            for word in words:
                all_words.append(word)
        #Counting the wrds and calling the word count writer
        word_count = len(all_words)
        word_counter_writer(word_count, filepath, lines)

def word_counter_writer(word_count, filepath, lines):
    line_count = len(lines)
    if "Word Count:" in lines[line_count - 1]:
        #If the file has already been counted
        with open(filepath, "w") as file:
            lines[line_count - 1] = f"Word Count: {word_count - 3}"
            return
    else:
        #If the file has not been counted
        with open(filepath, "w") as file:
            lines[line_count - 1] = f"\nWord Count: {word_count}"
            return