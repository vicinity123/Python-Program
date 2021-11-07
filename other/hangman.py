# Imports
from words_list import words
from word_state import word_state
import random
import string

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
alphabet = list(string.ascii_lowercase)
attempts_left = 6
correct_input = False
input_list = []

# Instructions
print(
    f"\nWelcome to the game of hangman. Each time this script is run, a new word will be generated for you to guess.\nThis script is case insensitive. Type (qq) to exit the script.\nFor this script the word you are looking for a word that contains {len(word)} letters."
)

# Initial state of the word - filled with hyphens
for i in enumerate(word):
    word_guess.append("-")

# Print start state
# print(word)
print("".join(word_guess))


# Game Logic
def hangman():
    # Correct or incorrect guess bool value
    global correct_input, attempts_left
    correct_input = word_state(user_input, word, word_guess)

    # Printing the current state
    print("".join(word_guess))

    # Taking attempts when wrong guess
    if not correct_input:
        attempts_left -= 1

    # Displaying the amount of attempts left
    print(f"Attempts left: {attempts_left}")

    # Ending the game once attempt equals 0
    if attempts_left == 0:
        print("End of game")
        print(word)
        quit()


# Game loop
while True:
    # Continuous user input
    user_input = input("\nGuess: ").lower()
    input_list.append(user_input)
    print(f"Used letters: {', '.join(set(input_list))}")

    # Quiting game if user input equals (qq)
    if user_input == "qq":
        quit()
    # If user input is valid, run game logic
    elif user_input in alphabet:
        hangman()
