# Imports
from words_list import words
from word_state import word_state
import random

# Get a valid word from words list
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
correct_input = False

# Instructions
print(
    f"\nWelcome the game of hangman. Each time this script is run, a new word will be generated for you to guess.\nThis script is case insensitive. Type (qq) to exit the script.\nFor this script the word you are looking for a word that contains {len(word)} letters."
)

for i in enumerate(word):
    word_guess.append("-")

# Print start state
print("Options: " + ", ".join(alphabet))
print(word)
print("".join(word_guess))


# Game Logic
def hangman():
    word_state(user_input, word, word_guess, correct_input)
    print(correct_input)
    print("".join(word_guess))

    global attempts_left

    if not correct_input:
        attempts_left -= 1

    print(f"Attempts left: {attempts_left}")

    if attempts_left == 0:
        print("End of game")
        quit()


# Game loop
while True:
    user_input = input("Guess: ")
    if user_input == "qq":
        quit()
    elif user_input in alphabet:
        hangman()
