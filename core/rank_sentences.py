from math import floor
import random


def rank_sentences(base_form_sentences, word_ranking, ranking_aging):
    sentences_count = len(base_form_sentences)

    indices = list(range(0, sentences_count))

    random.shuffle(indices)

    sentences_ranked = []
    for index in indices:
        sentence_base_words = base_form_sentences[index]
        ranking = 0

        for base_word in sentence_base_words:
            ranking += word_ranking.get(base_word)

            word_ranking[base_word] = floor(
                word_ranking[base_word] * (100 - ranking_aging)) / 100

        ranking_normalized = ranking / len(sentence_base_words)

        ranked_pair = (sentence_base_words, ranking_normalized)
        sentences_ranked.append(ranked_pair)

    return sentences_ranked
