# Imports
from words_list import words
from word_state import word_state
import random

# Get a valid word from the words list
def get_valid_word():
    while True:
        valid_word = random.choice(words)
        if not ("-" in valid_word) or (" " in valid_word):
            break
    return valid_word


# Variables related to the word and user attempts
word = get_valid_word()
word_length = len(word)
word_guess = []
alphabet = list("abcdefghijklmnopqrstuvwxyz")
attempts_left = 6

# Instructions
print(
    f"\nWelcome the game of hangman. Each time this script is run, a new word will be generated for you to guess.\nThis script is case insensitive. Type (qt) to exit the script.\nFor this script the word you are looking for contains {word_length} letters."
)


def hangman():
    if user_input in word:
        pass


# Game loop
while True:
    for i in range(word_length):
        word_guess.append("-")
    blank_spaces = "".join(word_guess)
    print(blank_spaces)
    user_input = input("Guess: ")
