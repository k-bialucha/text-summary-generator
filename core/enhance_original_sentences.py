def enhance_original_sentences(original_sentences, sentences_ranked):
    original_sentences_ranked = []

    for index, sentence in enumerate(original_sentences):
        ranking = sentences_ranked[index][1]

        sentence_data = (sentence, ranking, index)

        original_sentences_ranked.append(sentence_data)

    return original_sentences_ranked
