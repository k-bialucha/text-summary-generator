def rank_sentences(base_form_sentences, word_rank):
    sentences_ranked = []
    for sentence_base_words in base_form_sentences:
        ranking = 0

        for base_word in sentence_base_words:
            ranking += word_rank.get(base_word)

        ranking_normalized = ranking / len(sentence_base_words)

        ranked_pair = (sentence_base_words, ranking_normalized)
        sentences_ranked.append(ranked_pair)

    return sentences_ranked
