import re


def remove_blocked_words(base_words, ignored):
    ignored_words = ignored.split()
    allowed_words = list()

    for word in base_words:
        if word not in ignored_words:
            allowed_words.append(word)

    return allowed_words
