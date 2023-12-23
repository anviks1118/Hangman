"""
Hangman

Users guess the word. We give and validate the letters they give.

Us (developers)
- we need to give a random word for the user: √
    - store a list of possible words (in a text file) √
    - select a word from the text file randomly √
- check the user's guess:
    - if the letter is in the word and hasn't been guessed: 
        - fill in the blank with the letter
        - write down: "Correct letter!"
    - if the letter is not in the word and hasn't been guessed:
        - write down: "Sorry, incorrect letter!"
        - add a body part
    - if the letter is already guessed:
        - let users know the letter is already guessed (have it continuously display at the top):
        - at the top, mark which letters have been incorrectly guessed *
        - notify the user if a letter has already been guessed (string)
- draw the body parts individually once the user gets a letter incorrect √
- let the user know if they won or lost:
    - Win: when they guess the word (fill in all the blanks)
    - Lose: when they use all the body parts (order: head, body (stick), left arm, right arm, left leg, right leg)

Users
- guess a random letter √
"""

import random

# A function to change the board (add body parts) whenever the user guesses incorrectly.
# input = number of incorrect guesses (n)
# output = board
def board (n):
    # 0 mistakes
    if (n == 0):
        print ("  ______ \n |      |\n        |\n        |\n        |\n        |\n _______|______")

    # 1 mistake
    elif (n == 1):
        print ("  ______ \n |      |\n O      |\n        |\n        |\n        |\n _______|______")
    
    # 2 mistakes
    elif (n == 2):
        print ("  ______ \n |      |\n O      |\n |      |\n        |\n        |\n _______|______")
    
    # 3 mistakes
    elif (n == 3):
        print ("  ______ \n |      |\n O      |\n/|      |\n        |\n        |\n _______|______")

    # 4 mistakes
    elif (n == 4):
        print ("  ______ \n |      |\n O      |\n/|\     |\n        |\n        |\n _______|______")

    # 5 mistakes
    elif (n == 5):
        print ("  ______ \n |      |\n O      |\n/|\     |\n/       |\n        |\n _______|______")

    # 6 mistakes
    elif (n == 6):
        print ("  ______ \n |      |\n O      |\n/|\     |\n/ \     |\n        |\n _______|______")


# function to check if the user's guess is valid
def guess_valid(user_guess) -> bool:
    if "a" <= user_guess.lower() <= "z":
        return True
    else:
        return False


######## Main ########
# Pick a random word
with open("words.txt") as word_file:
    words = word_file.read().split()
    
random_word = random.choice(words)
mistakes = 6


# user's input
user_guess = input ("Guess a letter: ")
user_guess.lower()

while (guess_valid(user_guess) is False):
    user_guess = input ("Guess a valid letter: ")

