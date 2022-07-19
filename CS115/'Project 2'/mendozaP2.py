"""
Program: CS115 Project 2
Author: Erika Garnica Mendoza
Description: This program generates a match card game.
"""

from match_graphics import *
import random


def shuffle_cards():
    """
    Generates a shuffled deck of cards. When done, cards[i][j] is the name
    of the card in row i and column j. It is a 5x5 grid comprised of 12
    card pairs and one extra card.

    :param: None
    :return: cards
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

    :param: win, card_name, i, j
    :return: None
    """

    # Draw a rectangle with a yellow border of line width 5
    #  at the location associated with card (i,j)
    #  Ex: card (0,0) has upper-right corner (XMARGIN, YMARGIN) and
    #   lower-right corner (XMARGIN+CARD_WIDTH, YMARGIN+CARD_HEIGHT)
    x_ = i * CARD_WIDTH + XMARGIN
    y_ = j * CARD_HEIGHT + YMARGIN

    rectangle_top_left = Point(x_, y_)
    rectangle_bottom_right = Point(x_ + CARD_WIDTH, y_ + CARD_HEIGHT)

    # draws the yellow outlined rectangles filled with light green
    rectangle = Rectangle(rectangle_top_left, rectangle_bottom_right)
    rectangle.setOutline("yellow")
    rectangle.setFill("lightGreen")
    rectangle.setWidth(5)
    rectangle.draw(win)

    # Draws the image for card_name at the center of the rectangle.
    card = Image(Point(x_ + (CARD_WIDTH / 2), y_ + (CARD_HEIGHT / 2)), card_name[j][i])
    card.draw(win)

    return


def hide_card(win, i, j):
    """
    Takes the window and cards and hides the card at row i and column j.

    :param: win, i, j
    :return: None
    """

    x_ = i * CARD_WIDTH + XMARGIN
    y_ = j * CARD_HEIGHT + YMARGIN

    rectangle_top_left = Point(x_, y_)
    rectangle_bottom_right = Point(x_ + CARD_WIDTH, y_ + CARD_HEIGHT)

    # draws the yellow outlined rectangles filled with light green
    rectangle = Rectangle(rectangle_top_left, rectangle_bottom_right)
    rectangle.setOutline("yellow")
    rectangle.setFill("lightGreen")
    rectangle.setWidth(5)
    rectangle.draw(win)

    return


def mark_card(win, i, j):
    """
    Takes the window and cards and marks the card at row i and column j
    with a red X.

    :param: win, i, j
    :return: None
    """

    x_ = i * CARD_WIDTH + XMARGIN
    y_ = j * CARD_HEIGHT + YMARGIN

    top_left_point = Point(x_, y_)
    bottom_right_point = Point(x_ + CARD_WIDTH, y_ + CARD_HEIGHT)

    top_right_point = Point(x_ + CARD_WIDTH, y_)
    bottom_left_point = Point(x_, y_ + CARD_WIDTH)

    # draws the top left to bottom right diagonal line
    line = Line(top_left_point, bottom_right_point)
    line.setFill("red")
    line.setWidth(5)
    line.draw(win)

    # draws the top right to bottom left diagonal line
    line = Line(top_right_point, bottom_left_point)
    line.setOutline('red')
    line.setWidth(5)
    line.draw(win)

    return


def get_col(x):
    """
    Takes the x-coordinate value and returns the column.
    If the x coordinate is outside the board, returns -1.

    :param: x -integer
    :return: None
    """

    col_num = (x - XMARGIN) // CARD_WIDTH
    if 0 <= col_num <= 4:
        return col_num
    if x < XMARGIN or x > (BOARD_HEIGHT - XMARGIN):
        return -1


def get_row(y):
    """
    Takes the y-coordinate value and returns the row.
    If the y-coordinate is outside the board, returns -1.

    :param: y -integer
    :return: None
    """

    row_num = (y - YMARGIN) // CARD_HEIGHT
    if 0 <= row_num <= 4:
        return row_num
    if y < YMARGIN or y > (BOARD_WIDTH - YMARGIN):
        return -1


def main():
    """
    Generate a window consisting of shuffled cards in a 5x5 arrangement that are hidden,
    then accepts user clicks on each card and if they match it marks the pairs with a red X,
    once the user has found all the pairs it calls the you_won(win) function from match_graphics.py
    to flash random colors along the border of the game board.
    """

    # generate game window
    win = create_board()

    # shuffle the cards
    cards = shuffle_cards()

    # draw the 5x5 board with the cards on it
    for i in range(5):
        for j in range(5):
            # For Checkpoint B, edit to place them face-down
            hide_card(win, i, j)
            # For Checkpoint A, we place them face-up
            # show_card(win, cards[i][j], i, j)

    pairs = []  # to be able to have two cards match together
    mouse_clicks = 0  # starter before user clicks any cards
    while True:
        point = win.getMouse()  # get a mouse click

        x_point = point.getX()
        y_point = point.getY()

        row1 = int(get_row(y_point))
        column1 = int(get_col(x_point))

        if (column1, row1) in pairs:
            continue
        if row1 == -1 or column1 == -1:
            continue
        show_card(win, cards, column1, row1)  # show the card

        if mouse_clicks == 0:
            row2 = row1
            column2 = column1
        mouse_clicks += 1

        if mouse_clicks >= 2:  # two cards clicked

            if row1 == row2 and column1 == column2:
                continue
            game_delay(1)  # Pause for a second and figure out if the first pick and second pick are a match.

            if cards[row2][column2] == cards[row1][column1]:  # If first and second pick match, leave face up
                image_one = (column1, row1)
                image_two = (column2, row2)
                pairs.append(image_one)
                pairs.append(image_two)
                # if we have a 'matched pair' mark both pairs as matched
                mark_card(win, column2, row2)
                mark_card(win, column1, row1)
            else:
                # both cards are hidden if not a match
                hide_card(win, column1, row1)
                hide_card(win, column2, row2)
            if len(pairs) == 24:
                you_won(win)  # if we got here, then we won // so, call the you_won function.
                win.close()

            mouse_clicks = 0  # stops any extra clicks or singular clicks


main()
