"""
Program: CS 115 Lab 6b
Author: Erika Garnica Mendoza
Description: Computes the average word length of the user's text.
"""


def main():
    # Ask the user for some text, and save the text to a variable.
    text = input("Enter some text: ")
    # Convert the user's text into a list of words
    split_text = text.split()

    characterTotal = 0
    wordTotal = 0

    if text == '':
        # If user presses enter with a blank line
        print("You did not enter any words.")

    # As long as the user's text is not a blank line
    while text != '':

        characterTotal1 = len(text) - text.count(" ")
        wordTotal1 = len(split_text)

        # Gets new text from user, splits it into words
        text = input("Enter some text: ")
        # and saves it the same variable
        split_text = text.split()

        # previous total words and characters add to the next
        characterTotal += characterTotal1
        wordTotal += wordTotal1

        if len(split_text) == 0:
            # Prints the total amount of words for the user's input
            print("The average word length is: ", round(characterTotal / wordTotal, 5), sep='')

main()
