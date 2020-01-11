import re


def remove_blocked_words(sentences, blocked):
    blocked_words = blocked.split()

    for blocked_word in blocked_words:
        pattern = re.compile(blocked_word, re.IGNORECASE)
        for index, sentence in enumerate(sentences):
            sentences[index] = pattern.sub("", sentence)

    return sentences
