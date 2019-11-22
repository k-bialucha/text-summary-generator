from math import floor


def rank_sentences(base_form_sentences, word_ranking, ranking_aging):
    sentences_ranked = []
    for sentence_base_words in base_form_sentences:
        ranking = 0

        for base_word in sentence_base_words:
            ranking += word_ranking.get(base_word)

            word_ranking[base_word] = floor(
                word_ranking[base_word] * (100 - ranking_aging)) / 100

        ranking_normalized = ranking / len(sentence_base_words)

        ranked_pair = (sentence_base_words, ranking_normalized)
        sentences_ranked.append(ranked_pair)

    return sentences_ranked
