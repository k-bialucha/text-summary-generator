def rank_sentences(base_form_sentences, word_rank):
    sentences_ranked = []
    for sentence_base_words in base_form_sentences:
        ranking = 0

        for base_word in sentence_base_words:
            ranking += word_rank.get(base_word)

        ranked_pair = (sentence_base_words, ranking)
        sentences_ranked.append(ranked_pair)

    return sentences_ranked
