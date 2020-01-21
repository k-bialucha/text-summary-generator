from core.convert_to_base_words import convert_to_base_words
from core.create_word_ranking import create_word_ranking
from core.rank_sentences import rank_sentences
from core.enhance_original_sentences import enhance_original_sentences
from core.create_summary import create_summary
from core.remove_blocked_words import remove_blocked_words


def summarize(input_sentences, percent, aging, start_range, start_weight, end_range, end_weight, debug, ignore, use_special_words):
    base_form_sentences = []

    sentences = remove_blocked_words(input_sentences, ignore)

    for sentence in sentences:
        base_words = convert_to_base_words(sentence)
        base_form_sentences.append(base_words)

    word_ranking = create_word_ranking(base_form_sentences, use_special_words)

    sentences_ranked = rank_sentences(
        base_form_sentences, word_ranking, aging)

    original_sentences_ranked = enhance_original_sentences(
        sentences, sentences_ranked, [(0, start_range, start_weight), (100 - end_range, 100, end_weight)])

    return create_summary(original_sentences_ranked, percent, debug)
