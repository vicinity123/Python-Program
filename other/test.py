def word_state(letter, word, array):
    list_word = list(word)
    for _, el in enumerate(list_word):
        if el == letter:
            array.append(letter)
        else:
            array.append("-")
    return "".join(array)
