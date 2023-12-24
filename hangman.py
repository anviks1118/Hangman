"""
Hangman

Users guess the word. We give and validate the letters they give.

 Us (developers)
- √ we need to give a random word for the user: 
    - √ store a list of possible words (in a text file) 
    - √ select a word from the text file randomly 
- check the user's guess:
    - √ if the letter is in the word and hasn't been guessed: 
        - √ fill in the blank with the letter 
        - √ write down: "Correct letter!" 
    - √ if the letter is not in the word and hasn't been guessed: 
        - √ write down: "Sorry, incorrect letter!" 
        - √ add a body part
    - if the letter is already guessed:
        - let users know the letter is already guessed (have it continuously display at the top):
        - at the top, mark which letters have been incorrectly guessed *
        - √ notify the user if a letter has already been guessed (string) 
- √ draw the body parts individually once the user gets a letter incorrect 
- let the user know if they won or lost:
    - √ Win: when they guess the word (fill in all the blanks) 
    - √ Lose: when they use all the body parts (order: head, body (stick), left arm, right arm, left leg, right leg) 
    - √ Guess one letter at a time 
    - Show which letters have been guessed 
    - √ Reveal the final word after a fail attempt of the user guessing the word 
Users
- √ guess a random letter 
"""

import random

# A function to change the board (add body parts) whenever the user guesses incorrectly.
# input = number of incorrect guesses (n)
# output = board
def board (n) -> None:
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
    user_guess = user_guess.lower()
    if ("a" <= user_guess <= "z") and (len(user_guess) == 1):
        return True
    else:
        return False


# function to fill in the blanks based on the random word
def blanks(random_word) -> list:
    length = len(random_word)
    dashes = []

    for i in range(length):
        # add blanks to an array to keep track of it's position
        dashes.append("__")
    
    return dashes

######## Main ########
# Introduction
print("===== Welcome to Hangman! =====")
print("You only have 6 valid tries to guess the word. You can only guess english letters.")
print("Good luck!")
print("===============================")

# Pick a random word
with open("words.txt") as word_file:
    words = word_file.read().split()
    
random_word = random.choice(words).lower()
mistakes = 0

print("The word is: " + random_word)
dashes = blanks(random_word)

guessed_letters = []

# Main gameplay
count = 0
while (mistakes < 6):
    print("===============================")
    if ((6 - mistakes) == 0) or ("__" not in dashes):
        break
    else:
        print("You have", (6 - mistakes), "tries left.")
        board(mistakes)
        print("\n")
        print(dashes)
    
    # Show the letters the user guessed
    print("Letters guessed:", guessed_letters.sort())
    
    # User's input
    user_guess = input ("Guess a letter: ")

    while (guess_valid(user_guess) is False):
        user_guess = input ("Guess a valid letter: ")
    
    # If user already guessed letter
    while user_guess in guessed_letters:
        print("You already guessed this letter! Try another one.")
        user_guess = input ("Guess a letter: ")

        while (guess_valid(user_guess) is False):
            user_guess = input ("Guess a valid letter: ")

    guessed_letters.append(user_guess)

    # Updating blanks
    for i in range (len(dashes)):
        if user_guess == random_word[i]:
            dashes[i] = user_guess
            count += 1 
    
    if (count == 0):
        mistakes += 1
        print("This letter is not in the word.")
    else:
        print("This letter is in the word!")
    
    count = 0

# Game over
print("===============================")
board(mistakes)
print("\n")
print(dashes)

if (mistakes == 6):
    print("Game over... womp womp")
    print ("The word was", random_word.upper())

elif (mistakes < 6) and ("__" not in dashes):
    print("You guessed the word!")
