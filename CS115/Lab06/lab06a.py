"""
Program: CS 115 Lab 6a
Author: Erika Garnica Mendoza
Description: This program finds $1.00 words.
"""

def main():
    # Ask the user for a word, and save the word to a variable.
    word = input("Enter a word: ")
    
    # Convert the user's word to lowercase
    lowercase_word = word.lower()
    
    # As long as the user's word is not 'quit'...
    while lowercase_word != 'quit':
        letter_sum = 0
        
        # for loop that iterates every letter of a word into Unicode value
        for word in lowercase_word:
            letter_sum += (ord(word) - 96)
        print('Your word is worth $', "{0:.2f}".format(letter_sum / 100), '.', sep='')
        
        if letter_sum == 100:
            print('Congratulations!')
        # Echo their word back to them
        
        # Get a new word from them, convert it to lowercase,
        word = input("Enter a word: ")
        # and save it to the same variable.
        lowercase_word = word.lower()
        
        
main()


