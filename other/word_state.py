def word_state(letter, word, array, correct):
    list_word = list(word)
    for index, element in enumerate(list_word):
        if element == letter:
            array[index] = letter
