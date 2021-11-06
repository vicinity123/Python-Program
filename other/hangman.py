from words_list import words
import random


def get_valid_word():
    while True:
        valid_word = random.choice(words)
        if not ("-" in valid_word) or (" " in valid_word):
            break
    return valid_word


word = get_valid_word()
word_length = len(word)
word_guess = []
alphabet = list("abcdefghijklmnopqrstuvwxyz")

print(
    f"\nWelcome the game of hangman. Each time this script is run, a new word will be generated for you to guess.\nThis script is case insensitive. Type (qt) to exit the script.\nFor this script the word you are looking for contains {word_length} letters."
)

while True:
    user_input = input("Guess: ")
    for i in range(word_length):
        word_guess.append("-")
    if user_input in alphabet:
        break

print(
    f"Word: {word}\nWord length: {word_length}\nNumber of blank spaces: {word_guess}\nLength of the blank spaces: {len(word_guess)}"
)
