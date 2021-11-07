def word_state(letter, word, array):
    global current
    array_len = [set(array), ""]

    list_word = list(word)
    for index, element in enumerate(list_word):
        if element == letter:
            array[index] = letter

    array_len[1] = set(array)
    if array_len[0] != array_len[1]:
        return True
    else:
        return False
