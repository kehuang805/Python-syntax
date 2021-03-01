def print_upper_words(word_list, must_start_with):
    """Prints every word in word list as uppercase"""
    for word in word_list:
        if word[0].lower() in must_start_with:
            print(word.upper())
    