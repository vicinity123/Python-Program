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
word_guess = []
alphabet = list("abcdefghijklmnopqrstuvwxyz")
attempts_left = 6

# Instructions
print(
    f"\nWelcome the game of hangman. Each time this script is run, a new word will be generated for you to guess.\nThis script is case insensitive. Type (qq) to exit the script.\nFor this script the word you are looking for contains {len(word)} letters."
)

for i in enumerate(word):
    word_guess.append("-")


print(word_guess)

# Game loop
while True:
    user_input = input("Guess: ")
    if user_input == "qq":
        quit()
    elif user_input in alphabet:
        word_state(user_input, word, word_guess)
        print("".join(word_guess))
