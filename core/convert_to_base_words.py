import morfeusz2

morfeusz = morfeusz2.Morfeusz()

word_types_to_drop = [
    'interj',
    'interp',
    'part',
    'prep',
    'brev'
]


def convert_to_base_words(sentence):
    analysis = morfeusz.analyse(sentence)

    sentenceWords = []

    prev_i = None

    for i, j, interpretation in analysis:
        # TODO: find out which base form take
        word = interpretation[1].split(':')[0]
        word_type = interpretation[2].split(':')[0]

        is_word_allowed = word_type not in word_types_to_drop

        if i != prev_i and is_word_allowed:
            sentenceWords.append(word)

        prev_i = i

    return sentenceWords
