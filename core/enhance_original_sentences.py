import random
from core.calculate_segment_boost import calculate_segment_boost


def enhance_original_sentences(original_sentences, sentences_ranked, segment_boost):
    original_sentences_ranked = []

    sentences_count = len(original_sentences)

    indices = list(range(0, sentences_count))

    for index in indices:
        sentence = original_sentences[index]
        ranking = sentences_ranked[index][1]

        boost = calculate_segment_boost(index, sentences_count, segment_boost)

        sentence_data = (sentence, ranking * boost, index)

        original_sentences_ranked.append(sentence_data)

    return original_sentences_ranked
