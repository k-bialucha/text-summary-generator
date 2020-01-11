def remove_blocked_words(sentences, blocked):
    blocked_words = blocked.split()

    for blocked_word in blocked_words:
        for index, sentence in enumerate(sentences):
            if blocked_word in sentence:
                sentences[index] = sentence.replace(blocked_word, '')

    return sentences

