"""
Program: CS115 Project 2 Checkpoint A
Author: Erika Garnica Mendoza
Description: This program generates a 5x5 grid compromised of 12 card pairs
             and one extra card all faced up.
"""

from match_graphics import *
import random


def shuffle_cards():
    """
    Generates a shuffled deck of cards. When done, cards[i][j] is the name
    of the card in row i and column j. It is a 5x5 grid comprised of 12
    card pairs and one extra card.

    TODO (Final): document the parameters and return value
    """

    # The idea of how we shuffle is the following:
    # (1) shuffle the images
    random.shuffle(images)
    # (2) pick out 12 of the images (these are the ones that will be pairs)
    deck = []
    # (3) pick out the 'extra image' (this is the one that will have no pair)
    for i in range(len(images) - 1):
        # (4) create a list with 2 of each pair and the extra image
        deck.append(images[i])
        deck.append(images[i])
    deck.append(images[-1])
    # (5) shuffle that list
    random.shuffle(deck)

    # use the list of these 25 shuffled cards to build a 5x5 array of cards
    cards = []
    counter = 0

    for i in range(5):
        row = []
        for j in range(5):
            item = deck[counter]
            row.append(item)
            counter += 1
        cards.append(row)
    return cards


def show_card(win, card_name, i, j):
    """
    Shows the card at row i and column j in the 5x5 grid in the window.

    TODO (Final): document the parameters and return value, following
    """

    # Draw a rectangle with a yellow border of line width 5
    #  at the location associated with card (i,j)
    #  Ex: card (0,0) has upper-right corner (XMARGIN, YMARGIN) and
    #   lower-right corner (XMARGIN+CARD_WIDTH, YMARGIN+CARD_HEIGHT)
    x_ = i * CARD_WIDTH + XMARGIN
    y_ = j * CARD_HEIGHT + YMARGIN

    rectangle_top_left = Point(x_, y_)
    rectangle_bottom_right = Point(x_ + CARD_WIDTH, y_ + CARD_HEIGHT)

    rectangle = Rectangle(rectangle_top_left, rectangle_bottom_right)
    rectangle.setOutline("yellow")
    rectangle.setFill("lightGreen")
    rectangle.setWidth(5)
    rectangle.draw(win)

    # Draw the image for card_name at the center of the rectangle.
    card = Image(Point(x_ + (CARD_WIDTH / 2), y_ + (CARD_HEIGHT / 2)), card_name)
    card.draw(win)

    return


def hide_card(win, i, j):
    """
    Takes the window and cards and hides the card at row i and column j.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    """

    # TODO (Checkpoint B): finish this function as described
    return


def mark_card(win, i, j):
    """
    Takes the window and cards and marks the card at row i and column j
    with a red X.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    """

    # TODO (Final): finish this function as described
    return


def get_col(x):
    """
    Takes the x-coordinate value and returns the column.
    If the x coordinate is outside the board, returns -1.

    TODO (Final): document the parameters and return value
    """

    # TODO (Checkpoint B): finish this function as described
    return 0


def get_row(y):
    """
    Takes the y-coordinate value and returns the row.
    If the y-coordinate is outside the board, returns -1.

    TODO (Final): document the parameters and return value, following
    the examples in match_graphics
    """

    # TODO (Checkpoint B): finish this function as described
    return 0


def main():
    """
    TODO (Final): describe how your main function works.
    """

    # generate game window
    win = create_board()

    # shuffle the cards
    cards = shuffle_cards()

    # draw the 5x5 board with the cards on it
    for i in range(5):
        for j in range(5):
            # For Checkpoint A, we place them face-up
            show_card(win, cards[i][j], i, j)
            # For Checkpoint B, edit to place them face-down

    # TODO (Checkpoint B): implement the below logic

    # until we win:
    # get a mouse click
    # figure out which card was clicked
    # if this is a 'first pick':
    # show the card
    # else, if this is a 'second pick':
    # show the card
    # wait 1 second
    # if we have a 'matched pair':
    # mark both pairs as matched (Final Code)
    # else:
    # hide both cards

    # if we got here, then we won
    # so, call the you_won function.

    win.getMouse()


main()
