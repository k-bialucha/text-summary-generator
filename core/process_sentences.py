from core.convert_to_base_words import convert_to_base_words
from core.create_word_ranking import create_word_ranking
from core.rank_sentences import rank_sentences
from core.enhance_original_sentences import enhance_original_sentences
from core.create_summary import create_summary


def process_sentences(input_sentences):
    base_form_sentences = []

    for sentence in input_sentences:
        base_words = convert_to_base_words(sentence)
        base_form_sentences.append(base_words)

    word_ranking = create_word_ranking(base_form_sentences)

    sentences_ranked = rank_sentences(base_form_sentences, word_ranking)

    original_sentences_ranked = enhance_original_sentences(
        input_sentences, sentences_ranked)

    return create_summary(original_sentences_ranked, 0.5)
