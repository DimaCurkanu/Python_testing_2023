def split_and_merge(string_, separator):
    words = string_.split()  # Split the input string into words by spaces
    merged_words = []

    for word in words:
        # Split each word into characters and join them back with the separator
        merged_word = separator.join(list(word))
        merged_words.append(merged_word)

    # Join all the resulting words back into a sentence with spaces
    result = ' '.join(merged_words)
    return result
