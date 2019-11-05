import morfeusz2

morfeusz = morfeusz2.Morfeusz()


def convert_to_base_words(sentence):
    analysis = morfeusz.analyse(sentence)

    sentenceWords = []

    prev_i = None

    for i, j, interpretation in analysis:
        # TODO: find out which base form take
        word = interpretation[1].split(':')[0]

        if i != prev_i:
            sentenceWords.append(word)
        prev_i = i

    return sentenceWords
