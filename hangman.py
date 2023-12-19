"""
Hangman

Users guess the word. We give and validate the letters they give.

Us (developers)
- we need to give a random word for the user:
    - store a list of possible words (in a text file)
    - select a word from the text file randomly
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
- draw the body parts individually once the user gets a letter incorrect
- let the user know if they won or lost:
    - Win: when they guess the word (fill in all the blanks)
    - Lose: when they use all the body parts (order: head, body (stick), left arm, right arm, left leg, right leg)

Users
- guess a random letter
"""