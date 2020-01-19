from math import floor
import random


def sortByOriginalOrder(val):
    return val[2]


def rank_sentences(base_form_sentences, word_ranking, ranking_aging):
    sentences_count = len(base_form_sentences)

    indices = list(range(0, sentences_count))

    # shuffle original indices
    # to get more fair ranking
    random.Random(999).shuffle(indices)

    sentences_ranked = []
    for index in indices:
        sentence_base_words = base_form_sentences[index]
        ranking = 0.0

        for base_word in sentence_base_words:
            ranking += floor(word_ranking[base_word])
            word_ranking[base_word] = floor(
                word_ranking[base_word] * (100 - ranking_aging)) / 100

        ranking_normalized = ranking / len(sentence_base_words)

        ranked_tuple = (sentence_base_words, ranking_normalized, index)
        sentences_ranked.append(ranked_tuple)

    # restore original order of sentences
    sentences_ranked.sort(key=sortByOriginalOrder)

    return sentences_ranked
