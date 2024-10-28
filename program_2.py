# Author: Andrew Bittner
# Date: 10/25/2024

# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def exit_sequence():
    # Function to keep console/window open until user ends program.
    input('\n\nPress [enter] to exit... ')

def word_separator(sentence, cap_words = None):
    # Initialize values.
    if cap_words is None:
        cap_words = []
    sentence_new = list(sentence)
    # Add spaces between words and change all characters to lowercase.
    offset = 0
    for ind in range(len(sentence)):
        if sentence[ind].isupper():
            if ind != 0:
                sentence_new[ind + offset] = sentence_new[ind + offset].lower()
                sentence_new.insert(ind + offset, ' ')
                offset +=1
    sentence_new = ''.join(sentence_new)
    # Capitalize words.
    # sentence_new = sentence_new.replace(sentence_new[0], sentence_new[0].upper())
    for word in cap_words:
        if word.lower() in sentence_new:
            sentence_new = sentence_new.replace(word.lower(), word)
    print(sentence_new)
    return sentence_new

def main():
    sentence = 'IWentToNewYorkInJuly.'
    sentence_new = word_separator(sentence, ['New York', 'July'])
    print(sentence_new)

if __name__ == '__main__':
    main()